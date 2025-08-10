# SatelliteProcessor_mac.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('ml_models/checkpoints/*.pth', 'ml_models/checkpoints'),
        ('assets/*', 'assets'),
        ('config', 'config'),
    ],
    hiddenimports=[
        'torch',
        'torchvision',
        'gportal',
        'scipy.special._ufuncs_cxx',
        'scipy._lib.messagestream',
        'scipy.special.cython_special',
        'pkg_resources.py2_warn',
        'h5py._hl',
        'h5py._hl.base',
        'h5py._hl.files',
        'h5py._hl.group',
        'h5py._hl.dataset',
        'h5py.defs',
        'h5py.utils',
        'h5py.h5ac',
        'h5py._proxy',
        'matplotlib.backends.backend_tkagg',
        'PIL._tkinter_finder',
        'pyproj._datadir',
        'pyproj._network',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=['hook-pyproj.py'],
    excludes=['torch_directml'],  # Exclude Windows-specific module
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SatelliteProcessor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,  # UPX often causes issues on Mac
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/satellite_icon.icns',  # Mac icon format
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='SatelliteProcessor',
)

app = BUNDLE(
    coll,
    name='SatelliteProcessor.app',
    icon='assets/satellite_icon.icns',
    bundle_identifier='com.yourcompany.satelliteprocessor',
    info_plist={
        'NSHighResolutionCapable': 'True',
        'LSBackgroundOnly': 'False',
    },
)