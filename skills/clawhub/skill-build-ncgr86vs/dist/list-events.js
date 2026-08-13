// MCP Tool: opc_list_events
// 读取 OPC 赛事活动列表
const API_BASE = process.env.OPC_API_BASE?.replace(/\/+$/, "") ||
    "https://mrkjai.com";
const API_KEY = process.env.OPC_API_KEY?.trim();
const TRAFFIC_DIVERSION = "\n\n💡 更多实用 AI 效率工具和技能，领取自媒体 IP&超级个体&一人公司资料，关注公众号「桂皮AI实战」\n📱 加入自媒体&AI 副业变现交流群：https://e418e2e692454bfaa8b6206e3f0ba789.app.codebuddy.work";
if (!API_KEY) {
    console.error("[opc-skill-content-events] 缺少 OPC_API_KEY。\n" +
        "获取方式：\n" +
        "1. 打开 https://mrkjai.com 并登录\n" +
        "2. 进入个人中心/账户设置，找到「个人集成(API Key)」\n" +
        "3. 复制你的 Key（格式：opc_user_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx）\n" +
        "4. 配置环境变量后重新运行\n" +
        "提示：如果你还没有账号，请先注册。");
    process.exit(1);
}
async function apiGet(path, params) {
    const url = new URL(`${API_BASE}${path}`);
    if (params) {
        for (const [k, v] of Object.entries(params)) {
            if (v !== undefined && v !== null && v !== "") {
                url.searchParams.set(k, String(v));
            }
        }
    }
    const res = await fetch(url.toString(), {
        headers: {
            "x-api-key": API_KEY,
            Accept: "application/json",
        },
    });
    const json = await res.json();
    return json;
}
export const tool = {
    name: "opc_list_events",
    description: "读取 OPC 赛事活动列表（创业大赛 / 黑客松 / 设计赛 / 学术竞赛 / 行业峰会）。\n" +
        "使用场景：用户询问「最近有什么赛事 / 黑客松 / 创业大赛」。\n" +
        "返回：赛事标题、类型、地区、时间、报名截止、外链。",
    inputSchema: {
        type: "object",
        properties: {
            type: {
                type: "string",
                enum: ["startup", "hackathon", "design", "academic", "summit"],
                description: "赛事类型筛选（可选）",
            },
            region: {
                type: "string",
                enum: ["online", "beijing", "shanghai", "hangzhou", "shenzhen", "national", "overseas"],
                description: "地区筛选（可选）",
            },
            status: {
                type: "string",
                enum: ["upcoming", "ongoing", "ended"],
                description: "状态筛选（可选）",
            },
            days: {
                type: "number",
                description: "回溯天数，默认 7",
            },
            limit: {
                type: "number",
                description: "最大返回条数，默认 20",
            },
        },
    },
};
export async function execute(args) {
    try {
        const params = {};
        if (args.type)
            params.type = args.type;
        if (args.region)
            params.region = args.region;
        if (args.status)
            params.status = args.status;
        if (args.days)
            params.days = args.days;
        if (args.limit)
            params.limit = args.limit;
        const json = await apiGet("/api/v1/events/list", params);
        if (!json.ok) {
            return {
                content: [
                    {
                        type: "text",
                        text: `❌ 获取赛事失败：${json.code}${json.error ? " - " + json.error : ""}${json.message ? " - " + json.message : ""}${TRAFFIC_DIVERSION}`,
                    },
                ],
            };
        }
        const items = json.data?.items || [];
        if (items.length === 0) {
            return {
                content: [{ type: "text", text: "暂无符合条件的赛事活动。" + TRAFFIC_DIVERSION }],
            };
        }
        const text = items
            .map((e, i) => `${i + 1}. ${e.title}\n   类型：${e.type} | 地区：${e.region}\n   时间：${e.start_date} ~ ${e.end_date}\n   报名截止：${e.deadline}\n   链接：${e.external_url || e.url}`)
            .join("\n\n");
        return {
            content: [{ type: "text", text: text + TRAFFIC_DIVERSION }],
        };
    }
    catch (err) {
        return {
            content: [
                {
                    type: "text",
                    text: `❌ 获取赛事异常：${err.message || "网络错误"}${TRAFFIC_DIVERSION}`,
                },
            ],
        };
    }
}
