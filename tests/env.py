#Path hack to be able to run unit tests that refer to files in the src directory
import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
