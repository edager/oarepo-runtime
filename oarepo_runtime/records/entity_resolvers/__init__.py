from oarepo import __version__ as oarepo_version

from oarepo_runtime.records.entity_resolvers.proxies import DraftProxy

# compatibility setting between invenio rdm 11 and invenio rdm 12
# can be removed when invenio rdm 11 is no longer supported
if oarepo_version.split(".")[0] == "11":
    from invenio_users_resources.resolvers import UserResolver
    from invenio_records_resources.references import RecordResolver, EntityResolver
else:
    from invenio_users_resources.entity_resolvers import UserResolver
    from invenio_records_resources.references import RecordResolver, EntityResolver

__all__ = ["DraftProxy", "UserResolver", "RecordResolver", "EntityResolver"]
