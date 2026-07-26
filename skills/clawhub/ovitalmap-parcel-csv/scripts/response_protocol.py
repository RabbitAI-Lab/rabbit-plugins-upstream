"""Compact Chinese interaction guidance for OpenClaw and other agents."""


def build_response(run_id, step, result):
    guidance = _guidance(step, result)
    return {
        "run_id": run_id,
        "step": step,
        "status": guidance["status"],
        "next_action": guidance["next_action"],
        "required_input": guidance["required_input"],
        "reply_zh": guidance["reply_zh"],
        "result": result,
    }


def input_error_response(run_id, step, error):
    return {
        "run_id": run_id,
        "step": step,
        "status": "needs_input",
        "next_action": error.next_action,
        "required_input": error.required_input,
        "reply_zh": error.reply_zh,
        "error_code": error.code,
    }


def blocked_response(run_id, step, error):
    return {
        "run_id": run_id,
        "step": step,
        "status": "blocked",
        "next_action": "correct_input_or_retry",
        "required_input": [],
        "reply_zh": f"暂时无法继续处理：{error}",
        "error": str(error),
    }


def _guidance(step, result):
    if step == "1":
        return _step1_guidance(result)
    if step == "2b":
        return _step2b_guidance(result)
    if step == "2":
        return _step2_guidance(result)
    if step == "3":
        return _step3_guidance(result)
    raise ValueError(f"Unsupported response step: {step}")


def _step1_guidance(result):
    missing = []
    prompts = []
    coordinate_text = ""
    parcel_refs = result.get("parcel_refs", [])
    if not result.get("coordinates_confirmed"):
        missing.append("confirmed_coordinates")
        coordinate_text = "识别的 WGS84 坐标：\n" + "\n".join(
            f"- {parcel_refs[index - 1] if index <= len(parcel_refs) else f'P{index:02d}'}："
            + "；".join(
                f"{lon},{lat}" for lon, lat in vertices
            )
            for index, vertices in enumerate(
                result.get("coordinate_preview", []),
                start=1,
            )
        )
        prompts.append("请确认以上坐标与原始资料一致")
    if result.get("needs_country_confirmation"):
        missing.append("country_code")
        prompts.append("请提供或确认国家/地区")

    for index, provider in enumerate(result.get("provider_results", []), start=1):
        parcel_ref = (
            parcel_refs[index - 1] if index <= len(parcel_refs) else f"P{index:02d}"
        )
        field = f"provider_resolutions.{parcel_ref}"
        input_name = provider.get("input_name", "")
        candidates = provider.get("candidates", [])
        if not input_name:
            missing.append(field)
            prompts.append(f"请提供 {parcel_ref} 的提供者姓名")
        elif candidates and not provider.get("exact_match"):
            missing.append(field)
            names = "、".join(candidate["name"] for candidate in candidates)
            prompts.append(
                f"{parcel_ref} 的提供者“{input_name}”可能对应：{names}；"
                "请确认已有名称或明确作为新提供者"
            )

    if missing:
        body = "\n".join(f"- {prompt}" for prompt in prompts)
        sections = [section for section in [coordinate_text, body] if section]
        return {
            "status": "needs_input",
            "next_action": "confirm_preflight",
            "required_input": missing,
            "reply_zh": (
                "继续处理前需要确认以下关键信息：\n"
                + "\n".join(sections)
            ),
        }
    return {
        "status": "ready",
        "next_action": "run_step_2b",
        "required_input": [],
        "reply_zh": "坐标、国家/地区和提供者信息已确认，可以继续检查重复地块。",
    }


def _step2b_guidance(result):
    conflicts = result.get("batch_duplicate_conflicts", [])
    if conflicts:
        fields = [
            f"duplicate_resolutions.{item['parcel_ref']}" for item in conflicts
        ]
        lines = "\n".join(
            f"- {item['parcel_ref']} 与 {item['matches_ref']} 坐标相同："
            "回复 same（同一地块，跳过重复项）或 different（不同地块，分别归档）"
            for item in conflicts
        )
        return {
            "status": "needs_input",
            "next_action": "resolve_batch_duplicates",
            "required_input": fields,
            "reply_zh": f"发现批次内重复坐标：\n{lines}",
        }
    hit_count = result.get("archive_hit_count", 0)
    new_count = result.get("new_parcel_count", 0)
    next_action = "run_step_2" if new_count else "run_step_3"
    return {
        "status": "ready",
        "next_action": next_action,
        "required_input": [],
        "reply_zh": (
            f"重复检查完成：已有归档 {hit_count} 个，新地块 {new_count} 个。"
            + ("接下来为新地块分配编码。" if new_count else "无需分配新编码，可以生成文件。")
        ),
    }


def _step2_guidance(result):
    assigned = result.get("assigned_codes", [])
    if not assigned:
        return {
            "status": "ready",
            "next_action": "run_step_3",
            "required_input": [],
            "reply_zh": "没有需要分配编码的新地块，可以生成文件。",
        }
    code_lines = "\n".join(
        f"- {item.get('parcel_ref') or 'P%02d' % (item['index'] + 1)}："
        f"{item['parcel_code']}"
        for item in assigned
    )
    return {
        "status": "needs_input",
        "next_action": "confirm_codes",
        "required_input": ["confirmed_codes"],
        "reply_zh": f"已生成以下地块编码：\n{code_lines}\n请确认编码无误后再生成和归档文件。",
    }


def _step3_guidance(result):
    files = []
    new_result = result.get("new_csv_result")
    if new_result:
        refs = "、".join(
            ref for ref in new_result.get("parcel_refs", []) if ref
        )
        files.append(f"- 新地块批次{f'（{refs}）' if refs else ''}：")
        files.extend(_file_lines(new_result, "  "))
    for hit_result in result.get("hit_csv_results", []):
        identity = hit_result.get("parcel_ref") or hit_result.get("parcel_code")
        files.append(f"- 已有归档重导出{f'（{identity}）' if identity else ''}：")
        files.extend(_file_lines(hit_result, "  "))
    file_text = "\n".join(files) if files else "- 没有生成文件"
    archive = result.get("archive_result") or {}
    appended = archive.get("rows_appended", 0)
    return {
        "status": "completed",
        "next_action": "deliver_files",
        "required_input": [],
        "reply_zh": (
            f"处理完成，新增归档 {appended} 条。\n"
            f"{file_text}\n"
            "请下载对应文件并按顶点表“标签”、边界表“轨迹”导入奥维地图。"
        ),
    }


def _file_lines(result, indent=""):
    return [
        f"{indent}- 顶点表：{result['vertices_path']}",
        f"{indent}- 边界表：{result['boundary_path']}",
    ]
