import usb.core
import usb.util

class USB(object):

    def __init__(self):
        VENDOR_ID  = 0x0922
        PRODUCT_ID = 0x8003

        self.device = usb.core.find(idVendor=VENDOR_ID,
                                    idProduct=PRODUCT_ID)

        if self.device.is_kernel_driver_active(0):
            self.device.detach_kernel_driver(0)

        self.device.set_configuration()
        self.endpoint = self.device[0][(0,0)][0]


    def get_weight_grams(self):
        data = self.device.read(self.endpoint.bEndpointAddress,
                                self.endpoint.wMaxPacketSize)
        grams = data[4] + (256 * data[5])
        return grams
