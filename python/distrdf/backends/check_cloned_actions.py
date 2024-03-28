import numpy
import pytest

import ROOT


class TestAsNumpy:
    """
    Tests of proper functionality of the AsNumpy action across different
    distributed configurations.
    """

    @pytest.mark.parametrize("nparts", range(1, 21))
    def test_clone_asnumpyresult(self, payload, nparts):
        """
        Test that the correct values of the numpy array are retrieved from
        distributed execution irrespective of the number of partitions.
        """

        datasetname = "Events"
        filename = "../data/ttree/distrdf_roottest_check_cloned_actions_asnumpy.root"
        connection, backend = payload
        if backend == "dask":
            RDataFrame = ROOT.RDF.Experimental.Distributed.Dask.RDataFrame
            distrdf = RDataFrame(datasetname, filename,
                                 daskclient=connection, npartitions=nparts)
        elif backend == "spark":
            RDataFrame = ROOT.RDF.Experimental.Distributed.Spark.RDataFrame
            distrdf = RDataFrame(datasetname, filename,
                                 sparkcontext=connection, npartitions=nparts)

        localdf = ROOT.RDataFrame("Events", filename)

        vals_distrdf = distrdf.AsNumpy(["event"])
        vals_localdf = localdf.AsNumpy(["event"])

        assert all(vals_localdf["event"] == numpy.sort(vals_distrdf["event"]))


if __name__ == "__main__":
    pytest.main(args=[__file__])
