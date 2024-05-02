from dataclasses import dataclass

from dbt.adapters.base.relation import Policy
from dbt_common.dataclass_schema import StrEnum


class SynapseRelationType(StrEnum):
    Table = "table"
    View = "view"
    CTE = "cte"


class SynapseIncludePolicy(Policy):
    database: bool = True
    schema: bool = True
    identifier: bool = True


@dataclass
class SynapseQuotePolicy(Policy):
    database: bool = True
    schema: bool = True
    identifier: bool = True
