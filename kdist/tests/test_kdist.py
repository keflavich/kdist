from .. import kdist
import numpy as np

def test_scalar():
    d = kdist(43,0,7,near=False)
    np.testing.assert_almost_equal(d,11593.982050264149)
    d = kdist(48,0,55,near=True)
    np.testing.assert_almost_equal(d,4636.0775429302175)

def test_vector():
    d = kdist([43,48],[0,0],[7,55])
    np.testing.assert_array_almost_equal(d,np.array([692.76013694,  4636.07754293]))
    d = kdist([43,48],[0,0],[7,55],near=False)
    np.testing.assert_array_almost_equal(d,np.array([11593.98205026,   6605.3166439]))

def test_tangent():
    d = kdist([35]*10,[0]*10,np.linspace(-10,250,10))
    np.testing.assert_array_almost_equal(d,
                                         np.array([577.90781526,
                                                   1447.54058347,
                                                   3070.38114171,
                                                   4619.10988314,
                                                   6880.87717203,
                                                   6880.87717203,
                                                   6880.87717203,
                                                   6880.87717203,
                                                   6880.87717203,
                                                   6880.87717203])
                                         )
