# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..brains import BRAINSLandmarkInitializer


def test_BRAINSLandmarkInitializer_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputFixedLandmarkFilename=dict(argstr='--inputFixedLandmarkFilename %s',
    ),
    inputMovingLandmarkFilename=dict(argstr='--inputMovingLandmarkFilename %s',
    ),
    inputWeightFilename=dict(argstr='--inputWeightFilename %s',
    ),
    outputTransformFilename=dict(argstr='--outputTransformFilename %s',
    hash_files=False,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = BRAINSLandmarkInitializer.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BRAINSLandmarkInitializer_outputs():
    output_map = dict(outputTransformFilename=dict(),
    )
    outputs = BRAINSLandmarkInitializer.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
