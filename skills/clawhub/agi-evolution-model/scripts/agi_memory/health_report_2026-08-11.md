# AGI 进化模型 · 内部单元健康报告

生成时间：2026-08-11 00:30 (GMT+8)
运行环境：Windows / Python 3.13.14（managed）
人格：塔斯 / 谨慎探索型

---

## 总体结论

| 项目 | 结果 |
|------|------|
| 单元导入/运行 | **25/25 模块可加载**（修复 1 处崩溃后） |
| 单元测试（记录层/数学节点） | 全部 PASS |
| 健康检查器整体状态 | **degraded**（修复后，1 项可选依赖缺失） |
| 本次修复 | 2 处真实 bug |

---

## 一、各工具箱验证明细

### 1. 记录层（三轨存储）✅
| 单元 | 结果 |
|------|------|
| dimension_tagger（五维标签） | PASS |
| elevation_advisor（升维建议） | PASS |
| dimension_storage（五维存储） | PASS |
| cognitive_error_detector（认知错误检测） | PASS |
| cognitive_error_integration（集成） | PASS |
| error_wisdom_timeliness（时效性） | 运行正常（活跃0/弃用2/存档1） |
| error_wisdom_rule_generator（规则生成） | 运行正常（综合得分 0.45） |
| error_wisdom_prevention（预防引擎） | PASS（check 返回 pass:true） |
| error_wisdom_manager（管理器） | 正常（stats 可用） |
| memory_store_pure / history_manager | 导入正常 |

### 2. 数学节点工具箱 ✅
| 单元 | 结果 |
|------|------|
| objectivity_evaluator（客观性评估） | PASS（评分 0.82，场景适切） |
| cognitive_insight（认知洞察） | 导入正常 |

### 3. 映射层 ✅（修复后）
| 单元 | 结果 |
|------|------|
| personality_layer_pure（人格层） | **已修复**：导入崩溃 → 现优雅降级纯 Python（USE_C_EXT=False） |
| perception_node（感知节点） | 正常（C 扩展缺失，自动降级纯 Python，符合预期） |

### 4. 外环工程意向性模组 ✅
collector / classifier / analyzer / trigger / regulator / advice_pool / transcendence_keeper —— **全部导入正常**

### 5. CLI 工具箱 ✅
cli_file_operations / cli_system_info / cli_process_manager / cli_executor —— **全部导入正常**

### 6. 辅助模块 ✅
strategy_selector / concept_extraction_extension / metacognition_history / personality_customizer / cognitive_error_analyzer / logging_manager / metrics_collector / validation_framework —— **全部导入正常**

---

## 二、修复的真实缺陷

### BUG-1：`personality_layer_pure` 导入即崩溃（严重）
- **现象**：`AttributeError: 'NoneType' object has no attribute 'endswith'`
- **根因**：`personality_core` 是目录型命名空间包，`__file__` 为 `None`；代码直接对 `None` 调 `.endswith()`，且外层只 `except ImportError`，未兜住 `AttributeError`。
- **修复**：`module_path = getattr(personality_core, '__file__', None)`；`is_c_extension = bool(module_path) and (module_path.endswith('.so') or module_path.endswith('.pyd'))`
- **影响**：映射层人格层此前完全不可用，现已恢复并正确降级。

### BUG-2：`health_checker.disk_space` 在 Windows 误报 unhealthy（中等）
- **现象**：`module 'os' has no attribute 'statvfs'`，导致整体状态被误判为 unhealthy。
- **根因**：`os.statvfs` 是 Linux 专属 API。
- **修复**：改用跨平台 `shutil.disk_usage('.')`，并补 `import shutil`。
- **影响**：健康检查器自身不再产生假阴性，现正确报告磁盘 32.1% 已用（healthy）。

### BUG-3：`personality_core.so` 打包位置错误（跨平台，严重）
- **现象**：`import personality_core` 在 Windows 和 Linux 均拿不到 C 扩展，实际走纯 Python。
- **根因**：`.so` 被放在 `scripts/personality_core/` 子目录，而同名目录 `personality_core/` 被解析为命名空间包（`__file__=None`），`import personality_core` 永远命中目录而非 `.so`；导入逻辑又把 `scripts/personality_core/` 加进 `sys.path`，导致 `.so` 退化为子模块 `personality_core.personality_core` 而不可达。
- **验证**：WSL(Linux) 下 `import personality_core.personality_core` 报 "not a package"；但 `core_perception_node.so` 在把 `scripts/personality_core/` 加入 path 后能正常加载 → 证明 `.so` 本身是合法的 Linux C 扩展（ABI 兼容 Python 3.14）。
- **修复**：将 `scripts/personality_core/personality_core.so` 上移到 `scripts/personality_core.so`；`personality_layer_pure.py` 中 `core_dir` 由 `scripts/personality_core` 改为 `scripts`（使 `import personality_core` 命中根目录下的 `.so`）。
- **影响**：修复后路径/遮蔽问题已解决；但当时仅验证了 `import` 成功（误判 `USE_C_EXT=True`），**未验证执行**——见 BUG-4。
- 原 `core_perception_node.so` 布局本就正确，Linux 侧可直接加载且执行正常。

### BUG-4：`personality_core.so` 执行阶段 SIGILL（二进制/CPU 指令集不兼容，严重但此前被忽略）
- **现象**：WSL(Linux/Python 3.14) 下 `import personality_core` 成功、`calculate_similarity(...)` 调用时进程直接 `Illegal instruction`（SIGILL）崩溃；因崩溃发生在函数执行而非 import，原"符号齐全即视为可用"的判断会把它当可用扩展交给主进程，导致技能首次调用即整体崩溃。
- **根因**：预编译 `.so` 在编译机使用了当前 WSL 虚拟 CPU 不支持的 SIMD 指令（疑似 AVX-512 等）。`import` 阶段不触发该指令故不崩；执行 `calculate_similarity` 时触发 SIGILL。仓库**无 C 源码 / `setup.py` / `pyproject.toml`**，无法在本机重编译以匹配 CPU。
- **验证**：隔离测试 `CORE_LOADED True` 打印后 `CORE_CALL`/`CORE_DONE` 从未打印，bash 显式报告该 PID SIGILL；对照 `core_perception_node.generate_trace_id()` 执行正常返回真实 trace id → 确认是 `personality_core.so` 特有的二进制不兼容，而非路径/加载问题。
- **修复（终极方案核心）**：在集中加载器中加入**子进程执行探针**——加载并符号校验通过后，于独立子进程真实调用一次探针函数；子进程崩溃（SIGILL 等无法在主进程 `try/except` 捕获的错误）只影响自身，主进程据此判定该扩展不可用并降级到纯 Python。详见第五节。
- **影响**：本机 `personality_core` C 扩展被探测降级（仍由纯 Python 完整提供功能，速度较慢）；`core_perception_node` 通过探针保持启用。彻底消除"加载成功但执行炸进程"的隐患。

---

## 三、剩余待办（非缺陷）

- **[可选] 依赖 `aiofiles` 缺失** → 健康检查 `dependencies` 仍为 degraded。
  仅影响 Phase 0/1 异步化路径（memory_store_async 等），同步功能不受影响。
  如需清除：在 managed Python 环境 `pip install aiofiles>=23.0.0` 后重跑 `health_checker.py` 即转 healthy。
- **C 扩展的 Windows 可用性** → `personality_core.so` / `core_perception_node.so` 是 Linux ELF 格式，Windows 上无法加载（需 `.pyd`），故 Windows 侧始终走纯 Python（功能完整，约 1/15~1/20 速度）。
  **要在 Windows 拿到加速，需取得 C 源码并编译为 `.pyd`**——当前仓库不含源码/构建脚本，无法直接重编译。

### C 扩展可用性（修正）
- **Windows**：`.so` 格式不可加载，始终走纯 Python（功能完整，约 1/15~1/20 速度）。
- **WSL/Linux**：**仅 `core_perception_node.so` 可原生加载并安全执行**（`C_EXT_AVAILABLE=True`）；`personality_core.so` 因 CPU 指令集不兼容执行即 SIGILL，已被探针自动降级为纯 Python（`USE_C_EXT=False`）。
- **要在本机获得 `personality_core` 的 C 加速**：需取得 C 源码并针对本机 CPU 重新编译（如 `-march=x86-64` 或禁用不兼容的 SIMD）。当前仓库不含源码，无法重编译。

---

## 四、复核命令速查
```bash
# 健康检查
python scripts/health_checker.py

# 记录层单元自检
python scripts/dimension_tagger.py --test
python scripts/elevation_advisor.py --test
python scripts/dimension_storage.py --test
python scripts/cognitive_error_detector.py --test
python scripts/cognitive_error_integration.py --test

# 全模块导入冒烟测试
python -c "import sys; sys.path.insert(0,'.'); import importlib; [importlib.import_module(m) for m in ['personality_layer_pure','perception_node','intentionality_collector','cli_executor','cognitive_insight','memory_store_pure']]"
```

---

## 五、终极方案：C 扩展加载防错架构（防止"路径/加载"类问题再犯）

核心认知：**加载成功 ≠ 可用**。防错分三层：

**第 1 层 · 集中加载器 `c_ext_loader.py`（消除路径/遮蔽/平台错误）**
- 不用 `import <name>` 的解析顺序（会被同名目录型命名空间包遮蔽），改用 `importlib.util.spec_from_file_location` 按**显式文件路径**直接加载 `.so`/`.pyd`。
- 候选目录统一搜索：`scripts/` 根、`scripts/personality_core/`（兼容历史布局）、CWD。
- 平台感知后缀：posix→`.so`，win→`.pyd`。
- **必需符号校验**：加载后检查 `calculate_similarity` 等真实符号是否存在，确认拿到的是真 C 扩展而非占位命名空间包。
- 全程 `catch-all`，返回结构化 `(module, loaded, detail)`，**绝不向上抛未捕获异常**。

**第 2 层 · 执行安全探针（消除"加载成功但执行炸进程"）**
- `load_c_extension(..., runtime_probe=(函数名, 参数, 关键字))`：符号校验通过后，在**独立子进程**中真实调用一次探针函数。
- 子进程若 SIGILL/崩溃，只影响自己；主进程据此判定不可用并降级。
- 这是针对"预编译二进制与 CPU 指令集不兼容"的唯一可靠拦截手段（`try/except` 在主进程内无法捕获 SIGILL）。

**第 3 层 · 一致性布局 + 回归测试 + 健康检查**
- 布局统一：两个 `.so` 都置于 `scripts/` 根，删除空 `personality_core/` 目录，彻底消除命名空间包陷阱。
- 回归测试 `test_c_ext_loading.py`：双平台断言「消费者所选路径在主进程调用不崩溃」这一安全不变式；Windows 断言优雅降级，posix 断言「loaded=True 时必可执行」。
- 健康检查新增 `c_extensions` 项：复用同一加载器（含探针），posix 下扩展不可执行时如实报 `degraded`，绝不谎报 healthy。

**消费模块改造**：`personality_layer_pure.py` / `perception_node.py` 原分叉的 `sys.path` 插入 + `import` + `__file__.endswith` 逻辑，全部替换为 `c_ext_loader.load_c_extension(...)`，并始终绑定 `personality_core` / `core_perception_node` / `core_*` 别名指向"当前生效实现"，后续代码零改动。

## 六、双平台验证结果（终极方案落地后）

| 验证项 | Windows (py3.13) | WSL/Linux (py3.14) |
|------|------|------|
| 回归测试 `test_c_ext_loading.py` | 4/4 PASS（降级） | 4/4 PASS |
| `personality_core` C 扩展 | 优雅降级（无 .pyd） | 探针识别 SIGILL → 降级（纯 Python） |
| `core_perception_node` C 扩展 | 优雅降级（无 .pyd） | 真加载且执行正常（True） |
| `health_checker` c_extensions | healthy（预期） | degraded（已如实暴露） |
| 主进程调用不崩溃 | ✅ | ✅ |

复核命令：
```bash
# 回归测试（双平台通用，退出码非 0 即回归失败）
python scripts/test_c_ext_loading.py

# 加载器自测（含执行探针）
python scripts/c_ext_loader.py

# 健康检查（含 c_extensions 项）
python scripts/health_checker.py
```
