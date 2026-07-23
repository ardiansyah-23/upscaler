import torch

def get_device():

    if torch.cuda.is_available():

        return {
            "device":"CUDA",
            "name":torch.cuda.get_device_name(0)
        }

    elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():

        return {
            "device":"MPS",
            "name":"Apple Silicon"
        }

    else:

        return {
            "device":"CPU",
            "name":"Processor"
        }
