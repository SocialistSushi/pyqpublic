# pyqpublic
Python API for qPublic sites

This is a simple wrapper for qPublic sites. Right now it just handles basic searching.

## Basic Usage
```python
>>> from qpublic import QPublic
>>> qp = QPublic('BryanCountyGA')
>>> qp.searchByOwner('Jeffs Beverage')
>>> for parcel in qp.searchByOwner('Food'):
...     print parcel['owner'], parcel['propertyAddress']
... 
SAVANNAH SERVICE & FOOD LLC PO BOX 637 93 EXCHANGE ST
WOOLARD CLYDE FLASH FOODS HWY 17
```