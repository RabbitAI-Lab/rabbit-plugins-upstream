#!/bin/bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WS_DIR="$(cd "$SCRIPT_DIR/../../.." && pwd)"
PROFILES_DIR="$WS_DIR/docs/agent-profiles"

python3 << PYEOF
import json, os, glob
from datetime import datetime

profiles_dir = "$PROFILES_DIR"
agents = []

for f in sorted(glob.glob(os.path.join(profiles_dir, "*.json"))):
    if os.path.basename(f) == "index.json":
        continue
    try:
        with open(f) as fh:
            d = json.load(fh)
        agents.append({
            "systemName": d.get("systemName", ""),
            "displayName": d.get("displayName", ""),
            "role": d.get("role", ""),
            "layer": d.get("layer", ""),
            "pipelines": d.get("pipelines", []),
            "status": d.get("status", ""),
            "updatedAt": d.get("updatedAt", ""),
        })
    except Exception as e:
        print(f"⚠️  跳过 {os.path.basename(f)}: {e}")

index = {
    "generatedAt": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "totalAgents": len(agents),
    "byLayer": {},
    "byPipeline": {},
    "agents": agents,
}

for a in agents:
    layer = a.get("layer", "unknown")
    index["byLayer"].setdefault(layer, []).append(a["systemName"])

for a in agents:
    for p in a.get("pipelines", []):
        index["byPipeline"].setdefault(p, []).append(a["systemName"])

with open(os.path.join(profiles_dir, "index.json"), "w") as fh:
    json.dump(index, fh, ensure_ascii=False, indent=2)

print(f"✅ 索引已生成: {len(agents)} 个 Agent")
for k, v in index["byLayer"].items():
    print(f"   {k}: {len(v)} 个")
PYEOF
