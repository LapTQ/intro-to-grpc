from pathlib import Path
import sys

HERE = Path(__file__).parent
ROOT_DIR = HERE.parent.parent
sys.path.append(str(ROOT_DIR))

from src.protos.python.image_processing import image_processing_pb2_grpc, image_processing_pb2

# ==============================================================================

import pickle
import grpc
from concurrent import futures
import cv2


class ImageProcessingServicer(image_processing_pb2_grpc.ImageProcessor):

    def get_size(
            self,
            request,
            context
    ):
        img_pkl = request.img_pkl

        img = pickle.loads(img_pkl)
        H, W = img.shape[:2]

        print(f"Received image of size {W}x{H}")

        return image_processing_pb2.ImgSize(
            width=W,
            height=H
        )

    
    def show(
            self,
            request,
            context
    ):
        img_pkl = request.img_pkl
        window_name = request.window_name

        img = pickle.loads(img_pkl)
        cv2.imshow(window_name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print(f"Displayed image in window {window_name}")

        return image_processing_pb2.EmptyResponse()
    

    def resize(
            self,
            request,
            context
    ):
        img_pkl = request.img_pkl
        target_size = request.target_size
        H = target_size.height
        W = target_size.width

        img = pickle.loads(img_pkl)
        img = cv2.resize(img, (W, H))
        img_pkl = pickle.dumps(img)

        print(f"Resized image to {W}x{H}")

        return image_processing_pb2.FrameImg(
            img_pkl=img_pkl
        )
    


def serve():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )
    image_processing_pb2_grpc.add_ImageProcessorServicer_to_server(
        ImageProcessingServicer(),
        server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started, listening on 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
