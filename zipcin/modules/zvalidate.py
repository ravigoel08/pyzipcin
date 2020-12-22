from ..db import ZipDetail
from .base import session


def validate(pincode: int) -> bool:
    """
    Description
    -----------
    Verify if a pincode is correct or not:

    Parameters
    ----------
    pincode : int
        The pincode of district

    Returns
    -------
    bool
        True if pincode is corrent else False
    """

    try:
        int(pincode)
        value = session.query(ZipDetail).filter(ZipDetail.pincode == pincode).first()
        if value:
            return True
        else:
            return False
    except:
        return False
