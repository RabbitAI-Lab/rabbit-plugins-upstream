"""
类目级聚合与综合打分模块（v2）

设计原则：
1. scene_fitness 只反映"商品类型是否适合场景化"，不掺和市场图片风格
2. image_uniqueness_risk（图片同质化）和 ip_infringement_risk（法律 IP 侵权）拆开
3. ip_warning 命中高危词参与决策
4. 用 high_difficulty_ratio 捕捉 AI 难度的尾部风险
5. 经济性轻量参与决策（低销量/低客单价降级）
6. 输出 confidence 置信度
"""


# ============ IP 风险词库 ============
HIGH_RISK_IP_KEYWORDS = [
    "disney", "marvel", "nintendo", "pokemon", "star wars",
    "hello kitty", "sanrio", "pixar", "dc comics", "barbie",
    "sesame street", "paw patrol", "frozen elsa", "spiderman",
    "mickey mouse", "harry potter",
]
WALMART_PROHIBITED_KEYWORDS = [
    "firearm", "ammunition", "real gun", "handgun", "rifle",
    "cbd oil", "thc", "cannabis", "vape pen", "e-cigarette",
    "adult sexual", "erotic toy",
]
STRONG_CERT_KEYWORDS = [
    "infant", "toddler", "lithium battery", "battery pack",
    "medical device", "prescription",
]
BRAND_LOCKIN_KEYWORDS = [
    "dyson", "irobot", "roomba", "keurig", "nespresso",
    "kitchenaid", "ninja", "shark navigator", "bissell",
    "samsung", "lg ", "whirlpool", "ge appliance", "bosch", "miele",
]
COPYRIGHT_DESIGN_KEYWORDS = [
    "poster", "canvas print", "art print", "graphic tee",
    "phone case", "iphone case", "airpods case",
]


def score_category(products: list, vision_results: list) -> dict:
    valid_visions = [v for v in vision_results if v and "error" not in v]
    n = len(valid_visions)
    if n == 0:
        return _empty_score()
    if n < 5:
        return _insufficient_score(n)

    # ============ 1. 场景化适配度（纯商品形态判断，不混市场风格） ============
    scene_scores = [v.get("scene_fit_score", 50) for v in valid_visions]
    scene_fitness = sum(scene_scores) / n  # 0-100

    lifestyle_count = sum(
        1 for v in valid_visions
        if v.get("background_type") in ("lifestyle", "studio", "mixed")
    )
    white_count = sum(
        1 for v in valid_visions
        if v.get("background_type") in ("white_pure", "white_clean")
    )
    lifestyle_ratio = lifestyle_count / n  # 仅作参考输出，不计入 scene_fitness
    white_ratio = white_count / n

    # ============ 2. AI 改图难度（带尾部风险） ============
    difficulty_map = {"low": 1, "medium": 2, "high": 3}
    difficulties = [
        difficulty_map.get(v.get("ai_difficulty", "medium"), 2)
        for v in valid_visions
    ]
    avg_difficulty = sum(difficulties) / n
    high_count = sum(1 for d in difficulties if d == 3)
    high_difficulty_ratio = high_count / n

    if high_difficulty_ratio >= 0.5 or avg_difficulty > 2.3:
        difficulty_label = "高"
    elif high_difficulty_ratio >= 0.3 or avg_difficulty >= 1.7:
        difficulty_label = "中"
    else:
        difficulty_label = "低"

    # ============ 3. 拆分风险：图片同质化 vs IP 侵权 ============
    brand_count = sum(1 for v in valid_visions if v.get("has_brand_elements"))
    generic_count = sum(1 for v in valid_visions if v.get("is_generic_supplier_image"))
    watermark_count = sum(1 for v in valid_visions if v.get("has_text_watermark"))

    # 3a. 图片同质化（决定要不要改图）
    uniqueness_score = (generic_count * 3 + watermark_count) / (n * 4) * 100
    if uniqueness_score >= 50:
        uniqueness_risk = "🔴高"
    elif uniqueness_score >= 25:
        uniqueness_risk = "🟡中"
    else:
        uniqueness_risk = "🟢低"

    must_modify = generic_count >= n * 0.3 or watermark_count >= n * 0.4

    # 3b. IP 侵权（决定能不能搬）— 基于品牌物 + 关键词
    ip_warning_list, ip_severity = _check_ip_risk(products)
    ip_score = brand_count / n * 50 + ip_severity * 50  # 0-100
    if ip_score >= 60 or ip_severity >= 0.8:
        ip_risk = "🔴高"
    elif ip_score >= 30 or ip_severity >= 0.4:
        ip_risk = "🟡中"
    else:
        ip_risk = "🟢低"

    # 综合"侵权风险"显示（分开展示，不再合并）
    # infringement_risk 只反映法律 IP 风险，uniqueness_risk 单独展示
    risk_label = ip_risk

    # ============ 4. 商品形态 ============
    forms = [v.get("product_form", "unknown") for v in valid_visions]
    form_counter = {}
    for f in forms:
        form_counter[f] = form_counter.get(f, 0) + 1
    dominant_form = max(form_counter, key=form_counter.get) if form_counter else "unknown"

    non_scene_forms = {"replacement_part", "tool_hardware", "consumable", "electronic_device"}
    non_scene_ratio = sum(form_counter.get(f, 0) for f in non_scene_forms) / n

    # ============ 5. 经济性 ============
    prices = []
    for p in products:
        price = p.get("price")
        if price is not None:
            try:
                prices.append(float(price))
            except (ValueError, TypeError):
                pass
    median_price = sorted(prices)[len(prices) // 2] if prices else None

    sales_values = []
    for p in products:
        ms = p.get("monthly_sales")
        if ms:
            sales_values.append(_parse_sales(ms))
    median_sales = sorted(sales_values)[len(sales_values) // 2] if sales_values else None

    # 经济性预警
    economic_concern = None
    if median_price is not None and median_price < 8:
        economic_concern = "客单价过低"
    elif median_sales is not None and median_sales < 50:
        economic_concern = "销量偏低"

    # ============ 6. 改图策略 ============
    if non_scene_ratio >= 0.7 and scene_fitness < 40:
        strategy = "白底差异化改图" if must_modify else "保持白底"
    elif scene_fitness >= 60 and difficulty_label != "高":
        strategy = "全场景化"
    elif scene_fitness >= 40 and difficulty_label != "高":
        strategy = "主图白底+副图场景"
    elif must_modify and difficulty_label != "高" and scene_fitness >= 30:
        strategy = "主图白底+副图场景"
    elif must_modify and difficulty_label != "高":
        strategy = "白底差异化改图"
    else:
        strategy = "保持白底"

    # ============ 7. 决策逻辑 ============
    # 7.1 IP 侵权一票否决（高危直接弃）
    if ip_severity >= 0.8:
        decision = "❌弃"
        reason = f"IP/法律风险过高：{'; '.join(ip_warning_list[:2])}"
    # 7.2 IP 中危降级到谨慎（即使图片好也不能盲搬）
    elif ip_severity >= 0.4:
        if difficulty_label == "高":
            decision = "❌弃"
            reason = f"IP风险中-高 + AI难度高：{'; '.join(ip_warning_list[:2])}"
        else:
            decision = "⚠️谨慎(IP风险)"
            reason = f"存在IP/认证风险：{'; '.join(ip_warning_list[:2])}，需法务复核"
    # 7.3 替换件/工具/耗材 → 白底直搬
    elif non_scene_ratio >= 0.7 and scene_fitness < 40:
        decision = "✅白底直搬"
        reason = f"以{dominant_form}为主，白底搜索权重高"
    # 7.4 高难度 + 必须改图 = 弃
    elif must_modify and difficulty_label == "高":
        decision = "❌弃"
        reason = f"图片同质化{uniqueness_risk}必须改图，但AI难度高({high_difficulty_ratio*100:.0f}%高难图)"
    # 7.5 场景化高 + 难度可控 = AI 改图搬
    elif scene_fitness >= 60 and difficulty_label != "高":
        decision = "✅AI改图搬"
        reason = f"场景化适配{scene_fitness:.0f}分，AI难度{difficulty_label}，适合场景化改图"
    # 7.6 场景化中 + 必须改图 = AI 改图搬
    elif scene_fitness >= 40 and must_modify and difficulty_label != "高":
        decision = "✅AI改图搬"
        reason = f"场景化适配{scene_fitness:.0f}分，同质化{uniqueness_risk}必须改图，AI难度{difficulty_label}可行"
    # 7.7 场景化中 + 难度可控 = 可改图搬（正面推荐，非谨慎）
    elif scene_fitness >= 40 and difficulty_label != "高":
        decision = "✅可改图搬"
        reason = f"场景化适配{scene_fitness:.0f}分，AI难度{difficulty_label}，建议主图白底+副图场景"
    # 7.8 必须改图但场景不适合 = 谨慎需改图
    elif must_modify and difficulty_label != "高":
        decision = "⚠️谨慎(需改图)"
        reason = f"图片同质化{uniqueness_risk}必须改图，场景化适配低({scene_fitness:.0f}分)，建议白底改图"
    # 7.9 替换件兜底
    elif non_scene_ratio >= 0.7:
        decision = "✅白底直搬"
        reason = f"以{dominant_form}为主，场景化适配低，白底即可"
    # 7.10 场景化极低 = 白底直搬
    elif scene_fitness < 30:
        decision = "✅白底直搬"
        reason = f"场景化适配低({scene_fitness:.0f}分)，白底即可"
    else:
        decision = "⚠️谨慎"
        reason = f"场景化{scene_fitness:.0f}分，难度{difficulty_label}，需人工评估"

    # 7.11 经济性二次降级（除非已经是弃）
    if economic_concern and "✅" in decision:
        decision = decision.replace("✅", "⚠️") + f"({economic_concern})"
        reason = f"{reason}；但 {economic_concern}，建议先小批量测试"

    # ============ 8. 置信度 ============
    confidence_score = min(100, n * 2)  # 50张图=100分，5张=10分
    if confidence_score >= 80:
        confidence = "🟢强"
    elif confidence_score >= 40:
        confidence = "🟡中"
    else:
        confidence = "🔴弱"

    return {
        "scene_fitness": round(scene_fitness, 1),
        "ai_difficulty": difficulty_label,
        "ai_difficulty_avg": round(avg_difficulty, 2),
        "high_difficulty_ratio": round(high_difficulty_ratio, 2),
        "infringement_risk": risk_label,
        "uniqueness_risk": uniqueness_risk,
        "uniqueness_score": round(uniqueness_score, 1),
        "ip_risk": ip_risk,
        "ip_score": round(ip_score, 1),
        "ip_warning": "; ".join(ip_warning_list) if ip_warning_list else "",
        "must_modify_image": must_modify,
        "strategy": strategy,
        "decision": decision,
        "reason": reason,
        "dominant_form": dominant_form,
        "lifestyle_ratio": round(lifestyle_ratio, 2),
        "white_ratio": round(white_ratio, 2),
        "median_price": median_price,
        "median_sales": median_sales,
        "sample_count": n,
        "confidence": confidence,
        "economic_concern": economic_concern or "",
        "has_human_ratio": round(
            sum(1 for v in valid_visions if v.get("has_human")) / n, 2
        ),
    }


def _check_ip_risk(products: list):
    """
    返回 (warnings_list, severity 0-1)
    severity:
      0.0   无
      0.4   品牌垄断或图案版权（中危）
      0.8   IP 角色版权或强认证（高危）
      1.0   Walmart 禁售（顶格危）
    """
    all_text = " ".join([
        (p.get("title") or "") + " " + (p.get("brand") or "")
        for p in products
    ]).lower()

    warnings = []
    severity = 0.0

    sensitive_hits = [k for k in WALMART_PROHIBITED_KEYWORDS if k in all_text]
    if sensitive_hits:
        warnings.append(f"Walmart禁售({','.join(sensitive_hits[:2])})")
        severity = max(severity, 1.0)

    ip_hits = [k for k in HIGH_RISK_IP_KEYWORDS if k in all_text]
    if ip_hits:
        warnings.append(f"IP版权({','.join(ip_hits[:2])})")
        severity = max(severity, 0.8)

    cert_hits = [k for k in STRONG_CERT_KEYWORDS if k in all_text]
    if cert_hits:
        warnings.append(f"强认证({','.join(cert_hits[:2])})")
        severity = max(severity, 0.8)

    brand_hits = [b for b in BRAND_LOCKIN_KEYWORDS if b in all_text]
    if len(brand_hits) >= 3:
        warnings.append(f"品牌垄断({','.join(brand_hits[:3])})")
        severity = max(severity, 0.4)

    copyright_hits = [k for k in COPYRIGHT_DESIGN_KEYWORDS if k in all_text]
    if copyright_hits:
        warnings.append(f"图案版权({','.join(copyright_hits[:2])})")
        severity = max(severity, 0.4)

    return warnings, severity


def _insufficient_score(n: int) -> dict:
    return {
        "scene_fitness": 0,
        "ai_difficulty": "样本不足",
        "ai_difficulty_avg": 0,
        "high_difficulty_ratio": 0,
        "infringement_risk": "样本不足",
        "uniqueness_risk": "样本不足",
        "uniqueness_score": 0,
        "ip_risk": "样本不足",
        "ip_score": 0,
        "ip_warning": "",
        "must_modify_image": False,
        "strategy": "样本不足",
        "decision": "⚠️数据不足",
        "reason": f"仅 {n} 张图（<5），样本量不足以判断，建议手动重抓",
        "dominant_form": "unknown",
        "lifestyle_ratio": 0,
        "white_ratio": 0,
        "median_price": None,
        "median_sales": None,
        "sample_count": n,
        "confidence": "🔴弱",
        "economic_concern": "",
        "has_human_ratio": 0,
    }


def _empty_score() -> dict:
    return {
        "scene_fitness": 0,
        "ai_difficulty": "未知",
        "ai_difficulty_avg": 0,
        "high_difficulty_ratio": 0,
        "infringement_risk": "未知",
        "uniqueness_risk": "未知",
        "uniqueness_score": 0,
        "ip_risk": "未知",
        "ip_score": 0,
        "ip_warning": "",
        "must_modify_image": False,
        "strategy": "无数据",
        "decision": "❌无数据",
        "reason": "未抓到有效商品或图片分析失败",
        "dominant_form": "unknown",
        "lifestyle_ratio": 0,
        "white_ratio": 0,
        "median_price": None,
        "median_sales": None,
        "sample_count": 0,
        "confidence": "🔴弱",
        "economic_concern": "",
        "has_human_ratio": 0,
    }


def _parse_sales(s) -> int:
    if isinstance(s, (int, float)):
        return int(s)
    s = str(s).strip().upper()
    if "K" in s:
        return int(float(s.replace("K", "")) * 1000)
    if "M" in s:
        return int(float(s.replace("M", "")) * 1000000)
    try:
        return int(float(s))
    except (ValueError, TypeError):
        return 0
