"""Flat-module shim for original capgen's ``ddt_library``.

``write_init_files.py`` imports ``VarDDT`` for a single ``isinstance``
test (``src/data/write_init_files.py``, in
``_find_and_add_host_variable``)::

    if hvar and hvar.is_ddt() and not isinstance(hvar, VarDDT):
        return missing_vars   # skip whole-DDT host variables

In original capgen a ``VarDDT`` is a *field inside* a DDT at any nesting
level, and ``is_ddt()`` is True for it as well as for a whole-DDT
variable -- hence the ``not isinstance`` half of the guard.

capgen has no such object.  DDT instances are flattened into the host
dictionary at parse time (``metadata/variable_resolver.py``,
``_flatten_ddt_instance``), so a DDT component arrives as an ordinary
``HostVarEntry`` leaf carrying an intrinsic ``type`` and an
``access_path`` such as ``phys_state%theta``; only the DDT instance
itself keeps a DDT ``type``.  Nothing capgen produces is ever a
``VarDDT``, so this class is deliberately never instantiated: the
``isinstance`` test is always False and the guard reduces to "skip
whole-DDT host variables", which is the behaviour the caller wants.

See ``capgen_compat/README.md`` for the layer contract and removal plan.
"""


class VarDDT:
    """Placeholder for original capgen's DDT-component variable class.

    Never instantiated -- capgen flattens DDT components into plain host
    entries, so no wrapper is ever a ``VarDDT``.  Exists so
    ``isinstance(hvar, VarDDT)`` evaluates (to False) instead of raising
    ``NameError``.
    """

    def __init__(self, *args, **kwargs):
        raise NotImplementedError(
            "capgen_compat.ddt_library.VarDDT is a placeholder for an "
            "isinstance() check and is never instantiated: capgen "
            "flattens DDT components into the host dictionary, so there "
            "is no DDT-component variable object to construct."
        )


__all__ = ['VarDDT']
