#!/usr/bin/env python3
"""
防爆阀透气量计算与选型工具 v2

功能模块：
1. 温度变化透气量计算 (基于压差变化率驱动模型)
2. 海拔变化透气量计算 (基于压差驱动模型)
3. 压差-透气量曲线插值
4. 防爆阀选型推荐

v2 改进：
- 温度/海拔统一为「压差驱动」模型：透气速率 ∝ 压差变化率
- 显式计算单位压差变化率下的透气速率 (flow coefficient)
- 中间过程量完整输出，便于验证
"""

import json
import sys
from dataclasses import dataclass, field
from typing import Optional

# ============================================================
# 常量
# ============================================================
KELVIN_OFFSET = 273.15         # 摄氏度转开尔文
STD_ATMOSPHERE = 101.325       # 标准大气压 (kPa)
VALVE_RATED_PRESSURE = 7.0     # 防爆阀额定压差 (kPa)


# ============================================================
# 核心公式: 压差驱动的透气速率
# ============================================================
#
# 物理模型: 理想气体 PV = nRT, V 恒定
#
# ▸ 温度变化场景 (恒外压 P_atm):
#   温度变化 dT → 若密闭则产生 dP = P_atm × dT/T (等容过程)
#   阀体呼吸以维持恒压 → 需排/进气 dV = V0 × dT/T (等压过程)
#
#   透气速率与压差变化率成正比:
#     Φ = dV/dt = V0/T × dT/dt = V0/P_atm × dP/dt
#
#   其中 dP/dt = P_atm/T × dT/dt 为密闭时的理论压差变化率
#
#   → 单位压差变化率下的透气速率 (flow coefficient):
#     K = Φ / (dP/dt) = V0 / P_atm   [L/min per kPa/min]
#
#   → 任意压差 P_rated 下的需求透气量:
#     Φ_rated = K × P_rated = V0/P_atm × P_rated
#
# ▸ 海拔/外压变化场景 (恒温):
#   外压变化 dP_ext → 气体膨胀/收缩 dV = V0 × (-dP_ext)/P_ext
#   阀体呼吸以平衡内外压差
#
#   → 单位外压变化下的透气量:
#     K_alt = V0 / P   [L/min per kPa/min]
#     Φ_rated = V0/P × P_rated


def breathing_flow_coefficient(
    volume_l: float,
    reference_pressure_kpa: float = STD_ATMOSPHERE,
) -> float:
    """
    计算单位压差变化率下的透气速率系数。

    物理含义: 每 1 kPa/min 的压差变化率, 阀体需要呼吸多少 L/min 的气体。

    推导: K = V0 / P_ref
      - 温度场景: P_ref = 当地大气压 (呼吸维持恒压)
      - 海拔场景: P_ref = 当前环境气压 (气体膨胀/收缩的参考压力)

    参数:
        volume_l:              Pack 箱体净容积 (L)
        reference_pressure_kpa: 参考压力 (kPa), 默认为标准大气压

    返回:
        K (L/min per kPa/min)
    """
    return volume_l / reference_pressure_kpa


# ============================================================
# Sheet2 压差-透气量数据 (出厂标定曲线)
# ============================================================
VALVE_FLOW_CURVE = [
    (0.5, 0.326),    # (压差 kPa, 透气量 L/min)
    (1.0, 0.674),
    (1.5, 1.000),
    (2.0, 1.372),
    (2.5, 1.691),
    (3.0, 1.985),
]


def interpolate_flow(pressure_kpa: float) -> float:
    """线性插值: 给定压差 (kPa), 返回对应透气量 (L/min)"""
    curve = VALVE_FLOW_CURVE
    if pressure_kpa <= curve[0][0]:
        return pressure_kpa * curve[0][1] / curve[0][0]
    if pressure_kpa >= curve[-1][0]:
        slope = (curve[-1][1] - curve[-2][1]) / (curve[-1][0] - curve[-2][0])
        return curve[-1][1] + slope * (pressure_kpa - curve[-1][0])
    for i in range(len(curve) - 1):
        p0, q0 = curve[i]
        p1, q1 = curve[i + 1]
        if p0 <= pressure_kpa <= p1:
            return q0 + (q1 - q0) * (pressure_kpa - p0) / (p1 - p0)
    return 0.0


def interpolate_pressure(flow_lpm: float) -> float:
    """反插值: 给定透气量 (L/min), 返回对应压差 (kPa)"""
    curve = VALVE_FLOW_CURVE
    if flow_lpm <= curve[0][1]:
        return flow_lpm * curve[0][0] / curve[0][1]
    if flow_lpm >= curve[-1][1]:
        slope = (curve[-1][0] - curve[-2][0]) / (curve[-1][1] - curve[-2][1])
        return curve[-1][0] + slope * (flow_lpm - curve[-1][1])
    for i in range(len(curve) - 1):
        p0, q0 = curve[i]
        p1, q1 = curve[i + 1]
        if q0 <= flow_lpm <= q1:
            return p0 + (p1 - p0) * (flow_lpm - q0) / (q1 - q0)
    return 0.0


# ============================================================
# 温度变化透气量计算 (压差驱动模型)
# ============================================================

@dataclass
class TempBreathingResult:
    """温度变化透气量计算结果"""
    volume_l: float                         # 箱体体积 V0 (L)
    t0_c: float                             # 初始温度 (℃)
    t1_c: float                             # 终止温度 (℃)
    t0_k: float                             # 初始温度 (K)
    t1_k: float                             # 终止温度 (K)
    time_min: float                         # 时间 (min)
    # --- 中间过程量 ---
    temp_change_rate_c_per_min: float       # 温度变化率 dT/dt (℃/min)
    pressure_change_rate_kpa_per_min: float # 密闭时理论压差变化率 dP/dt (kPa/min)
    flow_coefficient_l_per_kpa: float       # 单位压差变化率的透气系数 K (L/min / kPa/min)
    # --- 结果 ---
    delta_v_l: float                        # 体积变化 ΔV (L)
    breathing_rate_lpm: float               # 透气量 Φ (L/min), 正值=排气, 负值=进气
    delta_p_sealed_kpa: float               # 假设密闭时的总压差 Δp (kPa)
    rated_flow_lpm: float                   # 标化透气量 @额定压差 (L/min)
    rated_pressure_kpa: float               # 额定压差 (kPa)

    def to_dict(self) -> dict:
        return {
            "volume_L": round(self.volume_l, 4),
            "T0_C": self.t0_c,
            "T1_C": self.t1_c,
            "T0_K": round(self.t0_k, 2),
            "T1_K": round(self.t1_k, 2),
            "time_min": self.time_min,
            "temp_change_rate_C_per_min": round(self.temp_change_rate_c_per_min, 4),
            "pressure_change_rate_kPa_per_min": round(self.pressure_change_rate_kpa_per_min, 6),
            "flow_coefficient_L_per_kPa": round(self.flow_coefficient_l_per_kpa, 6),
            "delta_V_L": round(self.delta_v_l, 4),
            "breathing_rate_L_per_min": round(self.breathing_rate_lpm, 6),
            "delta_p_sealed_kPa": round(self.delta_p_sealed_kpa, 4),
            "rated_flow_L_per_min": round(self.rated_flow_lpm, 6),
            "rated_pressure_kPa": self.rated_pressure_kpa,
            "direction": "排气(膨胀)" if self.delta_v_l > 0 else "进气(收缩)",
        }


def calc_temperature_breathing(
    volume_l: float,
    t0_c: float,
    t1_c: float,
    time_min: float,
    rated_pressure_kpa: float = VALVE_RATED_PRESSURE,
    p_atm_kpa: float = STD_ATMOSPHERE,
) -> TempBreathingResult:
    """
    计算因温度变化引起的透气量需求 (压差驱动模型)。

    物理过程:
      温度以速率 dT/dt 变化
      → 密闭时压差变化率 dP/dt = P_atm/T × dT/dt
      → 阀体呼吸速率 Φ = K × dP/dt = V0/P_atm × dP/dt
      → 标化至额定压差: Φ_rated = K × P_rated = V0/P_atm × P_rated

    步骤:
      1. 计算温度变化率 dT/dt 及对应的 dP/dt (密闭时压差变化率)
      2. 计算透气系数 K = V0/P_atm (L/min per kPa/min)
      3. Φ = K × dP/dt (实际透气速率)
      4. Φ_rated = K × P_rated (标化至额定压差)

    参数:
        volume_l:  Pack 箱体体积 (L)
        t0_c:      初始温度 (℃)
        t1_c:      终止温度 (℃)
        time_min:  温度变化时间 (min)
        rated_pressure_kpa: 防爆阀额定压差 (kPa), 默认 7.0
        p_atm_kpa: 当地大气压 (kPa), 默认 101.325

    返回:
        TempBreathingResult
    """
    t0_k = t0_c + KELVIN_OFFSET
    t1_k = t1_c + KELVIN_OFFSET

    # Step 1: 温度变化率及对应的压差变化率
    temp_change_rate = (t1_c - t0_c) / time_min                     # dT/dt (℃/min)
    pressure_change_rate = p_atm_kpa * temp_change_rate / t0_k       # dP/dt = P/T × dT/dt

    # Step 2: 透气系数 K = V0/P_atm
    flow_coeff = breathing_flow_coefficient(volume_l, p_atm_kpa)

    # Step 3: 实际透气速率 Φ = K × dP/dt
    # 同时等价于 Φ = V0/T × dT/dt = (V0 × (T1-T0)/T0) / t
    breathing_rate = flow_coeff * pressure_change_rate

    # Step 4: 标化透气量 @额定压差
    # Φ_rated = K × P_rated = V0/P_atm × P_rated
    rated_flow = flow_coeff * rated_pressure_kpa

    # 辅助量: 总压差 (密闭时) 和总体积变化
    delta_p_sealed = p_atm_kpa * (t1_k - t0_k) / t0_k
    delta_v = volume_l * (t1_k - t0_k) / t0_k

    return TempBreathingResult(
        volume_l=volume_l,
        t0_c=t0_c,
        t1_c=t1_c,
        t0_k=t0_k,
        t1_k=t1_k,
        time_min=time_min,
        temp_change_rate_c_per_min=temp_change_rate,
        pressure_change_rate_kpa_per_min=pressure_change_rate,
        flow_coefficient_l_per_kpa=flow_coeff,
        delta_v_l=delta_v,
        breathing_rate_lpm=breathing_rate,
        delta_p_sealed_kpa=delta_p_sealed,
        rated_flow_lpm=rated_flow,
        rated_pressure_kpa=rated_pressure_kpa,
    )


# ============================================================
# 海拔变化透气量计算 (压差驱动模型)
# ============================================================

@dataclass
class AltitudeBreathingResult:
    """海拔变化透气量计算结果"""
    volume_l: float                         # 箱体体积 (L)
    p0_kpa: float                           # 起始气压 (kPa)
    p1_kpa: float                           # 终止气压 (kPa)
    time_min: float                         # 时间 (min)
    # --- 中间过程量 ---
    pressure_change_rate_kpa_per_min: float # 外压变化率 dP_ext/dt (kPa/min)
    flow_coefficient_l_per_kpa: float       # 单位压差变化率的透气系数 K (L/min / kPa/min)
    # --- 结果 ---
    delta_p_kpa: float                      # 气压变化 ΔP (kPa)
    delta_v_l: float                        # 体积变化 ΔV (L)
    breathing_rate_lpm: float               # 透气量 Φ (L/min), 正值=排气, 负值=进气
    rated_flow_lpm: float                   # 标化透气量 @额定压差 (L/min)
    rated_pressure_kpa: float               # 额定压差 (kPa)

    def to_dict(self) -> dict:
        return {
            "volume_L": round(self.volume_l, 4),
            "P0_kPa": round(self.p0_kpa, 3),
            "P1_kPa": round(self.p1_kpa, 3),
            "time_min": self.time_min,
            "pressure_change_rate_kPa_per_min": round(self.pressure_change_rate_kpa_per_min, 6),
            "flow_coefficient_L_per_kPa": round(self.flow_coefficient_l_per_kpa, 6),
            "delta_P_kPa": round(self.delta_p_kpa, 3),
            "delta_V_L": round(self.delta_v_l, 4),
            "breathing_rate_L_per_min": round(self.breathing_rate_lpm, 6),
            "rated_flow_L_per_min": round(self.rated_flow_lpm, 6),
            "rated_pressure_kPa": self.rated_pressure_kpa,
            "direction": "排气(海拔上升/气压下降)" if self.delta_p_kpa < 0 else "进气(海拔下降/气压上升)",
        }


def calc_altitude_breathing(
    volume_l: float,
    p0_kpa: float,
    p1_kpa: float,
    time_min: float,
    rated_pressure_kpa: float = VALVE_RATED_PRESSURE,
) -> AltitudeBreathingResult:
    """
    计算因海拔/外压变化引起的透气量需求 (压差驱动模型)。

    物理过程:
      外压从 P0 变到 P1, 变化率 dP_ext/dt
      → 箱内气体等温膨胀/收缩: dV = V0 × (P0-P1)/P1 (等温过程)
      → 阀体呼吸速率 Φ = dV/dt
      → 透气系数 K = V0/P1 (使用终止压力作为参考, 因呼吸量在压力变化全过程中累积)
      → 标化至额定压差: Φ_rated = K × P_rated

    参数:
        volume_l:  Pack 箱体体积 (L)
        p0_kpa:    起始海拔对应气压 (kPa)
        p1_kpa:    终止海拔对应气压 (kPa)
        time_min:  海拔变化时间 (min)
        rated_pressure_kpa: 防爆阀额定压差 (kPa), 默认 7.0

    返回:
        AltitudeBreathingResult
    """
    delta_p = p1_kpa - p0_kpa  # 正值=外压升高, 负值=外压降低

    # 外压变化率
    pressure_change_rate = abs(delta_p) / time_min   # |dP_ext/dt| (kPa/min)

    # 透气系数: K = V0/P_end (使用结束时的气压作为最不利参考)
    # 海拔上升 (P0>P1): 气体膨胀, 参考压力使用较低值 P1
    # 海拔下降 (P0<P1): 气体收缩, 参考压力也应当使用较低值以取保守结果
    # 统一取 P0 和 P1 中较小值作为保守参考
    p_ref = min(p0_kpa, p1_kpa)
    flow_coeff = breathing_flow_coefficient(volume_l, p_ref)

    # 体积变化 (等温条件下)
    if abs(p0_kpa) > 1e-9:
        delta_v = volume_l * (p0_kpa - p1_kpa) / p1_kpa
    else:
        delta_v = 0.0

    # 透气速率
    breathing_rate = delta_v / time_min

    # 标化透气量 @额定压差
    # Φ_rated = K × P_rated = V0/P_ref × P_rated
    rated_flow = flow_coeff * rated_pressure_kpa

    return AltitudeBreathingResult(
        volume_l=volume_l,
        p0_kpa=p0_kpa,
        p1_kpa=p1_kpa,
        time_min=time_min,
        pressure_change_rate_kpa_per_min=pressure_change_rate,
        flow_coefficient_l_per_kpa=flow_coeff,
        delta_p_kpa=delta_p,
        delta_v_l=delta_v,
        breathing_rate_lpm=breathing_rate,
        rated_flow_lpm=rated_flow,
        rated_pressure_kpa=rated_pressure_kpa,
    )


# ============================================================
# 海拔-气压对照表 (标准大气模型, 每500m)
# ============================================================
ALTITUDE_PRESSURE_TABLE = {
    0: 101.325,
    500: 95.46,
    1000: 89.87,
    1500: 84.56,
    2000: 79.50,
    2500: 74.68,
    3000: 70.11,
    3500: 65.76,
    4000: 61.64,
    4500: 57.72,
    5000: 54.00,
}


def altitude_to_pressure(altitude_m: float) -> float:
    """海拔 (m) 转标准大气压 (kPa), 使用线性插值"""
    alts = sorted(ALTITUDE_PRESSURE_TABLE.keys())
    if altitude_m <= alts[0]:
        return ALTITUDE_PRESSURE_TABLE[alts[0]]
    if altitude_m >= alts[-1]:
        return ALTITUDE_PRESSURE_TABLE[alts[-1]]
    for i in range(len(alts) - 1):
        if alts[i] <= altitude_m <= alts[i + 1]:
            frac = (altitude_m - alts[i]) / (alts[i + 1] - alts[i])
            return ALTITUDE_PRESSURE_TABLE[alts[i]] + frac * (
                ALTITUDE_PRESSURE_TABLE[alts[i + 1]] - ALTITUDE_PRESSURE_TABLE[alts[i]]
            )
    return STD_ATMOSPHERE


# ============================================================
# 防爆阀选型
# ============================================================

@dataclass
class ValveCandidate:
    """候选阀门"""
    pressure_kpa: float
    flow_lpm: float
    required_flow_lpm: float
    cell_gas_lpm: float
    meets_breathing: bool
    meets_cell_gas: bool
    safety_factor: float

    @property
    def eligible(self) -> bool:
        return self.meets_breathing and self.meets_cell_gas


@dataclass
class ValveSelectionResult:
    """防爆阀选型结果"""
    required_flow_lpm: float
    cell_gas_rate_lpm: float
    rated_pressure_kpa: float
    candidates: list = field(default_factory=list)
    recommendation: str = ""

    def to_dict(self) -> dict:
        return {
            "required_flow_L_per_min": round(self.required_flow_lpm, 6),
            "cell_gas_rate_L_per_min": round(self.cell_gas_rate_lpm, 6),
            "rated_pressure_kPa": self.rated_pressure_kpa,
            "candidates": [
                {
                    "pressure_kPa": c.pressure_kpa,
                    "flow_L_per_min": round(c.flow_lpm, 4),
                    "required_flow_L_per_min": round(c.required_flow_lpm, 6),
                    "cell_gas_L_per_min": round(c.cell_gas_lpm, 6),
                    "meets_breathing": c.meets_breathing,
                    "meets_cell_gas": c.meets_cell_gas,
                    "safety_factor": round(c.safety_factor, 2),
                    "eligible": c.eligible,
                }
                for c in self.candidates
            ],
            "recommendation": self.recommendation,
        }


def select_valve(
    required_flow_lpm: float,
    cell_gas_rate_lpm: float = 0.0,
    rated_pressure_kpa: float = VALVE_RATED_PRESSURE,
    safety_margin: float = 1.5,
) -> ValveSelectionResult:
    """
    防爆阀选型。

    选型条件:
      1. 阀门在工作压差下的透气量 ≥ 温变/海拔所需透气量
      2. 阀门透气量 ≥ 电芯产气速率 (关键安全约束)
      3. 推荐安全系数 ≥ safety_margin
    """
    design_flow = max(required_flow_lpm, cell_gas_rate_lpm)
    candidates = []
    for p, q in VALVE_FLOW_CURVE:
        meets_breathing = q >= required_flow_lpm
        meets_cell_gas = q >= cell_gas_rate_lpm
        sf = q / design_flow if design_flow > 0 else float("inf")
        candidates.append(ValveCandidate(
            pressure_kpa=p, flow_lpm=q,
            required_flow_lpm=required_flow_lpm,
            cell_gas_lpm=cell_gas_rate_lpm,
            meets_breathing=meets_breathing,
            meets_cell_gas=meets_cell_gas,
            safety_factor=sf,
        ))

    recommendation = ""
    for c in candidates:
        if c.eligible and c.safety_factor >= safety_margin:
            recommendation = (
                f"推荐防爆阀工作压差 {c.pressure_kpa} kPa, "
                f"对应透气量 {c.flow_lpm:.3f} L/min, "
                f"安全系数 {c.safety_factor:.2f} >= {safety_margin}"
            )
            break

    if not recommendation:
        for c in reversed(candidates):
            if c.eligible:
                recommendation = (
                    f"推荐最大可选压差 {c.pressure_kpa} kPa, "
                    f"对应透气量 {c.flow_lpm:.3f} L/min, "
                    f"安全系数 {c.safety_factor:.2f} (偏低, 建议降低要求或多阀并联)"
                )
                break

    if not recommendation:
        max_flow = max(c.flow_lpm for c in candidates)
        recommendation = (
            f"现有阀门最大透气量 {max_flow:.3f} L/min 不满足需求 "
            f"({design_flow:.3f} L/min). 建议: 1)多阀并联; 2)增大箱体容积; "
            f"3)使用更大规格防爆阀"
        )

    return ValveSelectionResult(
        required_flow_lpm=required_flow_lpm,
        cell_gas_rate_lpm=cell_gas_rate_lpm,
        rated_pressure_kpa=rated_pressure_kpa,
        candidates=candidates,
        recommendation=recommendation,
    )


# ============================================================
# 综合计算入口
# ============================================================

@dataclass
class FullCalculationResult:
    """完整计算结果"""
    temp_cooling: Optional[TempBreathingResult] = None
    temp_heating: Optional[TempBreathingResult] = None
    alt_ascent: Optional[AltitudeBreathingResult] = None
    alt_descent: Optional[AltitudeBreathingResult] = None
    max_breathing_lpm: float = 0.0
    valve_selection: Optional[ValveSelectionResult] = None

    def to_dict(self) -> dict:
        result = {
            "max_breathing_rate_L_per_min": round(self.max_breathing_lpm, 6),
        }
        if self.temp_cooling:
            result["temperature_cooling"] = self.temp_cooling.to_dict()
        if self.temp_heating:
            result["temperature_heating"] = self.temp_heating.to_dict()
        if self.alt_ascent:
            result["altitude_ascent"] = self.alt_ascent.to_dict()
        if self.alt_descent:
            result["altitude_descent"] = self.alt_descent.to_dict()
        if self.valve_selection:
            result["valve_selection"] = self.valve_selection.to_dict()
        return result


def full_calculation(
    volume_l: float,
    t0_c: float,
    t1_c: float,
    temp_time_min: float,
    p0_kpa: float,
    p1_kpa: float,
    alt_time_min: float,
    cell_gas_rate_lpm: float = 0.0,
    rated_pressure_kpa: float = VALVE_RATED_PRESSURE,
    safety_margin: float = 1.5,
) -> FullCalculationResult:
    """
    综合计算: 温度变化 + 海拔变化 + 防爆阀选型。

    参数:
        volume_l:            Pack 箱体体积 (L)
        t0_c, t1_c:          温度范围 (℃)
        temp_time_min:       温度变化时长 (min)
        p0_kpa, p1_kpa:      海拔气压范围 (kPa), 可用 altitude_to_pressure() 转换
        alt_time_min:        海拔变化时长 (min)
        cell_gas_rate_lpm:   电芯产气速率 (L/min)
        rated_pressure_kpa:  防爆阀额定压差 (kPa)
        safety_margin:       安全系数
    """
    result = FullCalculationResult()

    result.temp_cooling = calc_temperature_breathing(
        volume_l, t0_c, t1_c, temp_time_min, rated_pressure_kpa
    )
    result.temp_heating = calc_temperature_breathing(
        volume_l, t1_c, t0_c, temp_time_min, rated_pressure_kpa
    )
    result.alt_ascent = calc_altitude_breathing(
        volume_l, p0_kpa, p1_kpa, alt_time_min, rated_pressure_kpa
    )
    result.alt_descent = calc_altitude_breathing(
        volume_l, p1_kpa, p0_kpa, alt_time_min, rated_pressure_kpa
    )

    flows = [
        abs(result.temp_cooling.rated_flow_lpm),
        abs(result.temp_heating.rated_flow_lpm),
        abs(result.alt_ascent.rated_flow_lpm),
        abs(result.alt_descent.rated_flow_lpm),
    ]
    result.max_breathing_lpm = max(flows)

    result.valve_selection = select_valve(
        required_flow_lpm=result.max_breathing_lpm,
        cell_gas_rate_lpm=cell_gas_rate_lpm,
        rated_pressure_kpa=rated_pressure_kpa,
        safety_margin=safety_margin,
    )

    return result


# ============================================================
# CLI 入口
# ============================================================

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print(__doc__)
        print("\n用法:")
        print("  python breathing_calc.py '<JSON>'")
        print("\nJSON 参数:")
        print(json.dumps({
            "volume_L": 20,
            "T0_C": 55,
            "T1_C": 20,
            "temp_time_min": 60,
            "P0_kPa": 101.325,
            "P1_kPa": 89.87,
            "alt_time_min": 60,
            "cell_gas_rate_L_per_min": 0.0,
            "rated_pressure_kPa": 7.0,
            "safety_margin": 1.5,
        }, indent=2, ensure_ascii=False))
        return

    if len(sys.argv) > 1:
        try:
            params = json.loads(sys.argv[1])
        except json.JSONDecodeError:
            print("错误: 无法解析 JSON 参数", file=sys.stderr)
            sys.exit(1)
    else:
        params = {}

    result = full_calculation(
        volume_l=params.get("volume_L", 20),
        t0_c=params.get("T0_C", 55),
        t1_c=params.get("T1_C", 20),
        temp_time_min=params.get("temp_time_min", 60),
        p0_kpa=params.get("P0_kPa", 101.325),
        p1_kpa=params.get("P1_kPa", 89.87),
        alt_time_min=params.get("alt_time_min", 60),
        cell_gas_rate_lpm=params.get("cell_gas_rate_L_per_min", 0.0),
        rated_pressure_kpa=params.get("rated_pressure_kPa", 7.0),
        safety_margin=params.get("safety_margin", 1.5),
    )

    print(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
