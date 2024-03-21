import os
import pickle
import glob

def create_directory_from_path(path):
    if os.path.exists(path):
        return
    os.makedirs(path, exist_ok=True)

def get_pickle_files_in_path(path):
    return glob.glob(os.path.join(path, '*.pkl'))

def update_cache(func):
    def wrapper(self, *args, **kwargs):
        output = func(self, *args, **kwargs)
        path = os.path.join(self.location, func.__name__.split('set_')[-1] + '.pkl')
        with open(path, 'wb') as outp:
            pickle.dump(getattr(self, func.__name__.split('set_')[-1]), outp, pickle.HIGHEST_PROTOCOL)
        return output
    return wrapper

def storable(location=None):
    def decorator(cls):
        class WrappedClass(cls):
            def __init__(self, *args, **kwargs):
                self.location = location
                create_directory_from_path(location)
                pickle_files = get_pickle_files_in_path(location)
                for file in pickle_files:
                    file_name = os.path.basename(file).split('set_')[-1].split('.pkl')[0]
                    setattr(self, file_name, self.unpack_pickle(file))
                super().__init__(*args, **kwargs)
            
            def unpack_pickle(self, file):
                 with open(file, 'rb') as outp:
                    return pickle.load(outp)

        for name, value in vars(cls).items():
            if name.startswith('set_') and callable(value):
                setattr(WrappedClass, name, update_cache(value))

        return WrappedClass
    return decorator