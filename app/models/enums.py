import enum

class ShippingType(enum.Enum):
    SEA = 'SEA'
    RAILWAY = 'RAILWAY'
    ROAD = 'ROAD'
    AIR = 'AIR'


class ParcelKind(enum.Enum):
    DOCUMENTS = 'DOCUMENTS'
    GOODS = 'GOODS'


class RequestStatus(enum.Enum):
    PENDING_REVIEW = 'PENDING_REVIEW'
    ACCEPTED = 'ACCEPTED'
    IN_TRANSIT = 'IN_TRANSIT'
    OUT_FOR_DELIVERY = 'OUT_FOR_DELIVERY'
    DELIVERED = 'DELIVERED'
    REJECTED = 'REJECTED'
