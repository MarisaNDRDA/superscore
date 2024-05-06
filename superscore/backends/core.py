"""
Base superscore data storage backend interface
"""
from typing import Generator
from uuid import UUID

from superscore.model import Entry


class _Backend:
    """
    Base class for data storage backend.
    """
    def get_entry(self, meta_id: UUID) -> Entry:
        """Get entry with ``meta_id``."""
        raise NotImplementedError

    def save_entry(self, entry: Entry):
        """
        Save ``entry`` into the database
        Throws BackendError if ``entry`` already exists
        """
        raise NotImplementedError

    def delete_entry(self, entry: Entry) -> None:
        """
        Delete ``entry`` from the system (all instances)
        """
        raise NotImplementedError

    def update_entry(self, entry: Entry) -> None:
        """
        Update ``entry`` in the backend.
        Throws BackendError if ``entry`` does not already exist
        """
        raise NotImplementedError

    def search(self, **search_kwargs) -> Generator[Entry, None, None]:
        """Yield a Entry objects corresponding matching ``search_kwargs``"""
        raise NotImplementedError
