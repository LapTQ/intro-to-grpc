from pathlib import Path
import sys

HERE = Path(__file__).parent
ROOT_DIR = HERE.parent.parent
sys.path.append(str(ROOT_DIR))

from src.protos.python.image_processing import image_processing_pb2_grpc, image_processing_pb2

# ==============================================================================

import pickle
import grpc
import numpy as np
import cv2


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = image_processing_pb2_grpc.ImageProcessorStub(channel)

        img = np.random.randint(0, 255, (256, 128, 3)).astype(np.uint8)
        img_pkl = pickle.dumps(img)
        
        img_size = stub.get_size(
            image_processing_pb2.FrameImg(
                img_pkl=img_pkl
            )
        )
        W = img_size.width
        H = img_size.height
        print(f"Image size: {W}x{H}")

        stub.show(
            image_processing_pb2.FrameData(
                img_pkl=img_pkl,
                window_name="Random Image"
            )
        )

        _ = stub.resize(
            image_processing_pb2.ResizeRequest(
                img_pkl=img_pkl,
                target_size=image_processing_pb2.ImgSize(
                    width=64,
                    height=64
                )
            )
        )
        img_pkl = _.img_pkl
        img = pickle.loads(img_pkl)
        print(f"Resized image to {img.shape[1]}x{img.shape[0]}")
        cv2.imshow("Resized Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    run()