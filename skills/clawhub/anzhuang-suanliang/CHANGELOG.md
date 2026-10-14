# 更新记录

## 0.4.10 — 2026-10-12（真图回归纳入发布预检）
- 新增 `scripts/run_preflight.sh`：全量自测 → 发布合规扫描 → 真图回归（复用 cad 底座，--manifest 强制），发布前统一入口。
- `ensure_base.sh` 保留 SHA-256 完整性校验；默认底座版本 cad-file-reader 0.28.5。

## 0.4.6 — 2026-10-12（底座自动安装加固）

- `ensure_base.sh` 增加 cad-file-reader 完整包 SHA-256 校验（从同 Release 下载 SHA256SUMS），校验失败拒绝安装与执行。
- 自动安装底座前校验包内 manifest 版本；默认底座版本升至 0.28.1。
- 平台安全扫描合规：自动下载底座改为带完整性校验、版本固定。



## 0.4.0 — 2026-10-05

对接 cad-file-reader 0.25.0 底座增强：旋转标注聚合、图例匹配、契约置信度/跨专业引用字段；版本门槛升至 `cad-file-reader >= 0.25.0`。


## 0.3.0 — 2026-10-05

对接 cad-file-reader 0.19/0.20 底座的 MEP 拓扑关联候选与交接校验。

- `mep_plan.py` 新增 `--mep-geometry`：可导入 cad-mep-geometry/v2 的 `mep_relations`（设备—管段、立管—管段、端点连接、系统冲突），进「MEP关联候选核对」工作表；候选固定 `final_quantity=false`，不参与本技能算量。
- `--cad-measurement` 导入前用 cad-file-reader `cad_validate.sh` 校验交接 JSON；校验失败只提示，不阻断。
- 自检扩展：覆盖 `mep_relations` 解析与空输入。


## 0.2.0 — 2026-09-20

- 对接 `cad-file-reader >= 0.18.0`，扫描结果记录底座版本和测量候选兼容状态。
- `mep_plan.py --cad-measurement` 支持导入“CAD测量候选核对”工作表；候选固定 `final_quantity=false`，不参与算量。
- 补充安装识图与算量边界说明，不输出金额、结算量或竣工计量。

## 0.1.0

- 首次发布安装算量技能。
- 支持 DWG 扫描索引与概算清单底稿、物资计划草稿双口径输出。
- 固化桥架 50m 异常单段阈值和剔除清单。
- 固化电线 `(路由长 + 两端预留) × 芯数` 展开。
- 增加规范约束、双口径映射、置信度分级、总量守恒和核对清单。
- 将 DWG 依赖重构为 `cad-file-reader` 动态发现，支持 `CAD_SKILL_DIR`。
