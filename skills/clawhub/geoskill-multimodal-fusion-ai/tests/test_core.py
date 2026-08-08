"""Core algorithm tests for multimodal-fusion-ai."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


def _best_perm_accuracy(pred, truth):
    """混淆矩阵 + 匈牙利最优一对一匹配后的像素精度。"""
    from sklearn.metrics import confusion_matrix
    from scipy.optimize import linear_sum_assignment
    labels = np.unique(np.concatenate([pred.ravel(), truth.ravel()]))
    cm = confusion_matrix(truth.ravel(), pred.ravel(), labels=labels).astype(float)
    r, c = linear_sum_assignment(-cm)
    return float(cm[r, c].sum() / cm.sum())


class TestStandardizeLayer:
    def test_minmax_range(self):
        x = np.array([[10.0, 20.0], [30.0, 40.0]])
        out = mod.standardize_layer(x, "minmax")
        assert out.min() == pytest.approx(0.0)
        assert out.max() == pytest.approx(1.0)
        # 单调性保持
        assert out[0, 0] < out[1, 1]

    def test_zscore_stats(self):
        rng = np.random.default_rng(0)
        x = rng.normal(50, 5, (100, 100))
        out = mod.standardize_layer(x, "zscore")
        assert out.mean() == pytest.approx(0.0, abs=1e-9)
        assert out.std() == pytest.approx(1.0, abs=1e-6)

    def test_constant_minmax_zero(self):
        out = mod.standardize_layer(np.full((4, 4), 7.0), "minmax")
        np.testing.assert_array_equal(out, 0.0)

    def test_constant_zscore_zero(self):
        out = mod.standardize_layer(np.full((4, 4), 3.0), "zscore")
        np.testing.assert_array_equal(out, 0.0)

    def test_bad_method(self):
        with pytest.raises(mod.UsageError):
            mod.standardize_layer(np.ones((3, 3)), "quantile")


class TestStandardizeLayers:
    def test_shape_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.standardize_layers([np.zeros((4, 4)), np.zeros((5, 5))])

    def test_empty_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.standardize_layers([])

    def test_all_standardized(self):
        layers = [np.random.uniform(0, 100, (8, 8)), np.random.uniform(-50, 0, (8, 8))]
        out = mod.standardize_layers(layers, "minmax")
        for o in out:
            assert o.min() >= 0.0 and o.max() <= 1.0


class TestEstimateNoise:
    def test_clean_vs_noisy(self):
        rng = np.random.default_rng(0)
        clean = np.zeros((64, 64))
        clean[:, 32:] = 0.5  # 分段常数，无噪声
        noisy = clean + rng.normal(0, 0.1, clean.shape)
        s_clean = mod.estimate_noise(clean)
        s_noisy = mod.estimate_noise(noisy)
        assert s_noisy > s_clean
        assert s_noisy == pytest.approx(0.1, rel=0.3)

    def test_tiny_image(self):
        assert mod.estimate_noise(np.zeros((1, 1))) == 0.0


class TestAutoWeights:
    def test_noisy_source_lower_weight(self):
        rng = np.random.default_rng(1)
        base = np.zeros((64, 64))
        base[:, 32:] = 1.0
        clean = base.copy()
        noisy = base + rng.normal(0, 0.3, base.shape)
        w = mod.auto_weights([clean, noisy])
        assert w[0] > w[1]  # 无噪声源权重更高
        assert w.sum() == pytest.approx(1.0)

    def test_all_constant_equal(self):
        w = mod.auto_weights([np.full((4, 4), 1.0), np.full((4, 4), 9.0)])
        np.testing.assert_allclose(w, [0.5, 0.5])

    def test_empty_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.auto_weights([])


class TestParseWeights:
    def test_valid_normalized(self):
        w = mod.parse_weights("3,1", 2)
        np.testing.assert_allclose(w, [0.75, 0.25])

    def test_count_mismatch(self):
        with pytest.raises(mod.UsageError):
            mod.parse_weights("1,2,3", 2)

    def test_negative(self):
        with pytest.raises(mod.UsageError):
            mod.parse_weights("1,-1", 2)

    def test_all_zero(self):
        with pytest.raises(mod.UsageError):
            mod.parse_weights("0,0", 2)

    def test_non_numeric(self):
        with pytest.raises(mod.UsageError):
            mod.parse_weights("a,b", 2)

    def test_empty(self):
        with pytest.raises(mod.UsageError):
            mod.parse_weights("  ", 2)


class TestFuseWeighted:
    def test_exact_average(self):
        a = np.zeros((4, 4))
        b = np.full((4, 4), 2.0)
        fused = mod.fuse_weighted([a, b], np.array([0.5, 0.5]))
        np.testing.assert_allclose(fused, 1.0)

    def test_weighted(self):
        a = np.full((3, 3), 0.0)
        b = np.full((3, 3), 4.0)
        fused = mod.fuse_weighted([a, b], np.array([0.25, 0.75]))
        np.testing.assert_allclose(fused, 3.0)

    def test_single_weight_dominant(self):
        a = np.full((3, 3), 1.0)
        b = np.full((3, 3), 9.0)
        fused = mod.fuse_weighted([a, b], np.array([1.0, 0.0]))
        np.testing.assert_allclose(fused, 1.0)

    def test_count_mismatch(self):
        with pytest.raises(mod.ValidationError):
            mod.fuse_weighted([np.zeros((3, 3))], np.array([0.5, 0.5]))

    def test_zero_weights(self):
        with pytest.raises(mod.ValidationError):
            mod.fuse_weighted([np.zeros((3, 3))], np.array([0.0]))

    def test_empty_layers(self):
        with pytest.raises(mod.ValidationError):
            mod.fuse_weighted([], np.array([]))


class TestJointClassify:
    def test_labels_range(self):
        img = np.zeros((30, 30))
        img[:, 10:20] = 0.5
        img[:, 20:] = 1.0
        labels = mod.joint_classify(img, n_classes=3)
        assert labels.shape == (30, 30)
        assert set(np.unique(labels)).issubset({0, 1, 2})

    def test_bad_n_classes(self):
        with pytest.raises(mod.UsageError):
            mod.joint_classify(np.zeros((4, 4)), n_classes=0)

    def test_rejects_3d(self):
        with pytest.raises(mod.ValidationError):
            mod.joint_classify(np.zeros((2, 4, 4)), n_classes=2)


class TestFuseAndClassify:
    def test_pipeline(self):
        rng = np.random.default_rng(0)
        layers = [rng.uniform(0, 1, (16, 16)), rng.uniform(0, 100, (16, 16))]
        fused, labels, info = mod.fuse_and_classify(layers, None, n_classes=3)
        assert fused.shape == (16, 16)
        assert labels.shape == (16, 16)
        assert info["n_layers"] == 2
        assert len(info["weights"]) == 2
        assert pytest.approx(sum(info["weights"])) == 1.0

    def test_weight_count_mismatch(self):
        layers = [np.zeros((4, 4)), np.zeros((4, 4))]
        with pytest.raises(mod.ValidationError):
            mod.fuse_and_classify(layers, np.array([0.5]), n_classes=2)


class TestAffineResidualStd:
    def test_recovers_noise_level(self):
        rng = np.random.default_rng(0)
        ref = rng.uniform(0, 1, 4096)
        x = 0.8 * ref + 0.1 + rng.normal(0, 0.05, ref.size)
        sigma = mod.affine_residual_std(x, ref)
        assert sigma == pytest.approx(0.05, rel=0.15)

    def test_perfect_copy_near_zero(self):
        ref = np.random.default_rng(1).uniform(0, 1, 1000)
        assert mod.affine_residual_std(ref, ref) < 1e-9

    def test_size_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.affine_residual_std(np.zeros(10), np.zeros(11))


class TestSyntheticFusion:
    def test_fusion_reduces_mse(self):
        """融合图对真值的 MSE 应小于任一单源（降噪）。"""
        layers, truth, _ = mod.generate_synthetic([116, 39, 117, 40], seed=7)
        fused, labels, info = mod.fuse_and_classify(layers, None, n_classes=3, seed=7)
        truth_std = mod.standardize_layer(truth.astype(np.float64), "minmax")
        std_layers = mod.standardize_layers(layers, "minmax")
        src_mse = [float(np.mean((s - truth_std) ** 2)) for s in std_layers]
        fused_mse = float(np.mean((fused - truth_std) ** 2))
        assert fused_mse < min(src_mse)

    def test_fusion_reduces_residual_noise(self):
        """扣除线性偏差后的残差噪声：融合应低于任一单源。"""
        layers, truth, _ = mod.generate_synthetic([116, 39, 117, 40], seed=9)
        fused, _, _ = mod.fuse_and_classify(layers, None, n_classes=3, seed=9)
        truth_std = mod.standardize_layer(truth.astype(np.float64), "minmax")
        std_layers = mod.standardize_layers(layers, "minmax")
        src_noise = [mod.affine_residual_std(s, truth_std) for s in std_layers]
        fused_noise = mod.affine_residual_std(fused, truth_std)
        assert fused_noise < min(src_noise)

    def test_fusion_classifies_better(self):
        """融合分类精度应不低于最优单源。"""
        layers, truth, _ = mod.generate_synthetic([116, 39, 117, 40], seed=11)
        fused, labels, _ = mod.fuse_and_classify(layers, None, n_classes=3, seed=11)
        acc_fused = _best_perm_accuracy(labels, truth)
        acc_single = []
        for l in layers:
            lab = mod.joint_classify(mod.standardize_layer(l, "minmax"), n_classes=3, seed=11)
            acc_single.append(_best_perm_accuracy(lab, truth))
        assert acc_fused >= max(acc_single) - 0.02
        assert acc_fused > 0.85

    def test_shapes(self):
        layers, truth, info = mod.generate_synthetic([116, 39, 117, 40])
        assert len(layers) == 2
        assert layers[0].shape == (64, 64)
        assert truth.shape == (64, 64)
        # 两模态量纲差异显著
        assert abs(layers[0].mean() - layers[1].mean()) > 1.0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "f.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
