from zope.interface import Interface

class IKitTemplate(Interface):
    """Comment"""

class IKitTemplates(Interface):
    """Comment"""

class IKits(Interface):
    """Package folder"""

class IKit(Interface):
    """Package Supply"""

class IStorageManagement(Interface):
    """Interface for Storage management"""

class IStorageManagements(Interface):
    """Interface for Storage managements"""

class IProject(Interface):
    """Interface for Project"""

class IProjects(Interface):
    """Interface for Projects"""

class IBiospecType(Interface):
    """Interface for Project"""

class IBiospecTypes(Interface):
    """Interface for Projects"""

class IShipments(Interface):
    """Interface for shipments"""

class IShipment(Interface):
    """Interface for a shipment"""

class IBiospecimen(Interface):
    """Interface for a biospecimen"""

class IBiospecimens(Interface):
    """Interface for a biospecimens"""

class IMultimage(Interface):
    """Interface for a multimage"""

class IAliquot(Interface):
    """Interface for a aliquot"""

class IAliquots(Interface):
    """Interface for aliquots"""

class IStorageInventory(Interface):
    """Interface for StorageInventory"""

class IStorageInventories(Interface):
    """Interface for StorageInventories"""

class IInventoryAssignable(Interface):
    """Interface for StorageInventories"""

class IStockItemStorageLocation(Interface):
    """A StorageLocation or StorageLevel that can store StockItems must
    provide this interface"""

class IBioSpecimenStorageLocation(Interface):
    """A StorageLocation or StorageLevel that can store BioSpecimen objects
     must provide this interface"""

class IAliquotStorageLocation(Interface):
    """A StorageLocation or StorageLevel that can store Aliquots must
    provide this interface"""

class IKitStorageLocation(Interface):
    """A StorageLocation or StorageLevel that can store Kits must
    provide this interface"""
