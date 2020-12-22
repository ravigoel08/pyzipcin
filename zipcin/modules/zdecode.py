from ..db import ZipDetail
from .base import session
from typing import List, Dict
from .constants import DC_OUT, MODE


def decode(pincode: int, all_result: bool = False) -> List[Dict[DC_OUT, MODE]]:
    """
    Description
    -----------
    for a PINCODE returns:

    'circlename'
    'regionname'
    'divisionname'
    'officename'
    'pincode'
    'officetype'
    'delivery'
    'district'
    'statename'

    officetype has 3 values:
    H.O. Head Post Office
    B.O. Branch Post Office
    S.O. Sub Post Office

    Parameters
    ----------
    pincode : int
        The pincode of district
    all_result : bool, optional
        Get all district information for a pincode (default
        is False)

    Returns
    -------
    list
        a list of dictionary's containing the information
        mentioned in description
    """

    try:
        int(pincode)
    except:
        return None

    if all_result:
        result = []
        values = session.query(ZipDetail).filter(ZipDetail.pincode == pincode)
        for val in values:
            result.append(val.as_dict())
        return result
    else:
        value = session.query(ZipDetail).filter(ZipDetail.pincode == pincode).first()
        if value:
            return [value.as_dict()]
        else:
            return None
