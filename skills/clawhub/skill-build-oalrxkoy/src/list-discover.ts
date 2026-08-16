// MCP Tool: opc_list_discover
// 读取 OPC 发现 / AI 羊毛列表

interface Args {
  type?: string;
  featured?: boolean;
  limit?: number;
}

const API_BASE =
  process.env.OPC_API_BASE?.replace(/\/+$/, "") ||
  "https://mrkjai.com";
const API_KEY = process.env.OPC_API_KEY?.trim();

const TRAFFIC_DIVERSION =
  "\n\n💡 更多实用 AI 效率工具和技能，领取自媒体 IP&超级个体&一人公司资料，关注公众号「桂皮AI实战」\n📱 加入自媒体&AI 副业变现交流群：https://e418e2e692454bfaa8b6206e3f0ba789.app.codebuddy.work";

if (!API_KEY) {
  console.error(
    "[opc-skill-content-discover] 缺少 OPC_API_KEY。\n" +
      "获取方式：\n" +
      "1. 打开 https://mrkjai.com 并登录\n" +
      "2. 进入个人中心/账户设置，找到「个人集成(API Key)」\n" +
      "3. 复制你的 Key（格式：opc_user_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx）\n" +
      "4. 配置环境变量后重新运行\n" +
      "提示：如果你还没有账号，请先注册。"
  );
  process.exit(1);
}

async function apiGet(path: string, params?: Record<string, string | number | undefined>): Promise<any> {
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
    } as Record<string, string>,
  });

  const json = await res.json();
  return json;
}

export const tool = {
  name: "opc_list_discover",
  description:
    "读取 OPC 发现 / AI 羊毛列表（深度种草、工具上手体验、一人公司效率兵器谱）。\n" +
    "使用场景：用户询问「最近有什么 AI 羊毛 / 效率工具 / 发现文章」。\n" +
    "返回：文章标题、摘要、分类、作者、发布时间、链接。",
  inputSchema: {
    type: "object",
    properties: {
      type: {
        type: "string",
        description: "分类筛选（可选），如 AI工具、效率、创业",
      },
      featured: {
        type: "boolean",
        description: "是否仅返回精选内容（可选）",
      },
      limit: {
        type: "number",
        description: "最大返回条数，默认 20",
      },
    },
  },
};

export async function execute(args: Args) {
  try {
    const params: Record<string, string | number | undefined> = {};
    if (args.type) params.type = args.type;
    if (args.featured !== undefined) params.featured = String(args.featured);
    if (args.limit) params.limit = args.limit;

    const json = await apiGet("/api/v1/discover", params);

    if (!json.ok) {
      return {
        content: [
          {
            type: "text",
            text: `❌ 获取发现失败：${json.code}${json.error ? " - " + json.error : ""}${json.message ? " - " + json.message : ""}${TRAFFIC_DIVERSION}`,
          },
        ],
      };
    }

    const items = json.data?.items || [];
    if (items.length === 0) {
      return {
        content: [{ type: "text", text: "暂无符合条件的发现文章。" + TRAFFIC_DIVERSION }],
      };
    }

    const text = items
      .map(
        (d: any, i: number) =>
          `${i + 1}. ${d.title}\n   分类：${d.category || "未分类"} | 作者：${d.author || "匿名"}\n   发布：${d.published_at}\n   摘要：${d.excerpt || "无摘要"}\n   链接：${d.url || `https://mrkjai.com/discover/${d.slug}`}`
      )
      .join("\n\n");

    return {
      content: [{ type: "text", text: text + TRAFFIC_DIVERSION }],
    };
  } catch (err: any) {
    return {
      content: [
        {
          type: "text",
          text: `❌ 获取发现异常：${err.message || "网络错误"}${TRAFFIC_DIVERSION}`,
        },
      ],
    };
  }
}
