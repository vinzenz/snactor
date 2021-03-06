from jsl import Scope
# Schema helpers


def after_version(version):
    return Scope(lambda v: v >= version)


def before_version(version):
    return Scope(lambda v: v < version)


def between_versions(version_first, version_last):
    return Scope(lambda v: v >= version_first and v <= version_last)
