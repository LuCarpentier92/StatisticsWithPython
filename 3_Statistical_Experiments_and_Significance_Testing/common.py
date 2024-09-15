from pathlib import Path


def dataDirectory(dataDirectoryName='data'):
    dataDir = Path(__file__).resolve().parent
    while not list(dataDir.rglob('data')):
        dataDir = dataDir.parent
    found = [d for d in dataDir.rglob('data') if d.is_dir()]
    if not found:
        raise Exception(f'Cannot find data directory with name {dataDirectoryName} along the path of your source files')
    return found[0]