from pathlib import Path
import pandas as pd

from visions.core.model.model_relation import relation_conf
from visions.core.model.models import tenzing_model


class tenzing_existing_path(tenzing_model):
    """**Existing Path** implementation of :class:`tenzing.core.models.tenzing_model`.
    >>> x = pd.Series([Path('/home/user/file.txt'), Path('/home/user/test2.txt')])
    >>> x in tenzing_existing_path
    True
    """

    @classmethod
    def get_relations(cls):
        from visions.core.model.types import tenzing_path

        relations = {tenzing_path: relation_conf(inferential=False)}
        return relations

    @classmethod
    def contains_op(cls, series: pd.Series) -> bool:
        return all(isinstance(p, Path) and p.exists() for p in series)
