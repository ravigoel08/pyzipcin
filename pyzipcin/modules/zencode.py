from ..db import ZipDetail, Base
from .base import session
from typing import List, Dict
from .constants import EN_OUT, MODE


def encode(districtname: str, all_result: bool = False) -> List[Dict[EN_OUT, MODE]]:
    """
    Description
    -----------
    for a districtname returns:

    'officename'
    'pincode'

    Parameters
    ----------
    districtname : str
        The name of district
    all_result : bool, optional
        Get all officename, pincode information for a district name (default
        is False)

    Returns
    -------
    list
        a list of dictionary's containing the information
        mentioned in description
    """

    if districtname.isalpha():
        pass
    else:
        return None
    if all_result:
        result = []
        values = session.query(ZipDetail).filter(
            ZipDetail.district == districtname.upper()
        )
        for val in values:
            val = val.as_dict()
            result.append({"pincode": val["pincode"], "officename": val["officename"]})
        return result
    else:
        value = (
            session.query(ZipDetail)
            .filter(ZipDetail.district == districtname.upper())
            .first()
        )
        if value:
            value = value.as_dict()
            return [{"pincode": value["pincode"], "officename": value["officename"]}]
        else:
            return None
