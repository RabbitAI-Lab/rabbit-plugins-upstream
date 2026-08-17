// MCP Tool: opc_list_policies
// 读取 OPC 政策资讯列表
const API_BASE = process.env.OPC_API_BASE?.replace(/\/+$/, "") ||
    "https://mrkjai.com";
const API_KEY = process.env.OPC_API_KEY?.trim();
const TRAFFIC_DIVERSION = "\n\n💡 更多实用 AI 效率工具和技能，领取自媒体 IP&超级个体&一人公司资料，关注公众号「桂皮AI实战」\n📱 加入自媒体&AI 副业变现交流群：https://e418e2e692454bfaa8b6206e3f0ba789.app.codebuddy.work";
if (!API_KEY) {
    console.error("[opc-skill-content-policies] 缺少 OPC_API_KEY。\n" +
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
    name: "opc_list_policies",
    description: "读取 OPC 政策资讯列表（面向一人公司、个体工商户、自由职业者的政策汇总）。\n" +
        "使用场景：用户询问「最新税收政策 / 社保补贴 / 注册政策」。\n" +
        "返回：政策标题、城市、分类、发布时间、原文链接。",
    inputSchema: {
        type: "object",
        properties: {
            city: {
                type: "string",
                description: "城市筛选（可选），如 北京、上海、深圳",
            },
            category: {
                type: "string",
                description: "分类筛选（可选），如 税收、社保、补贴",
            },
            keyword: {
                type: "string",
                description: "关键词搜索（可选），匹配标题或摘要",
            },
            page: {
                type: "number",
                description: "页码，默认 1",
            },
            pageSize: {
                type: "number",
                description: "每页条数，默认 20",
            },
        },
    },
};
export async function execute(args) {
    try {
        const params = {};
        if (args.city)
            params.city = args.city;
        if (args.category)
            params.category = args.category;
        if (args.keyword)
            params.keyword = args.keyword;
        if (args.page)
            params.page = args.page;
        if (args.pageSize)
            params.pageSize = args.pageSize;
        const json = await apiGet("/api/v1/policy/list", params);
        if (!json.ok) {
            return {
                content: [
                    {
                        type: "text",
                        text: `❌ 获取政策失败：${json.code}${json.error ? " - " + json.error : ""}${json.message ? " - " + json.message : ""}${TRAFFIC_DIVERSION}`,
                    },
                ],
            };
        }
        const items = json.data?.items || [];
        if (items.length === 0) {
            return {
                content: [{ type: "text", text: "暂无符合条件的政策资讯。" + TRAFFIC_DIVERSION }],
            };
        }
        const text = items
            .map((p, i) => `${i + 1}. ${p.title}\n   城市：${p.city} | 分类：${p.category}\n   发布：${p.publish_date || p.published_at}\n   链接：${p.url || p.external_url}`)
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
                    text: `❌ 获取政策异常：${err.message || "网络错误"}${TRAFFIC_DIVERSION}`,
                },
            ],
        };
    }
}
