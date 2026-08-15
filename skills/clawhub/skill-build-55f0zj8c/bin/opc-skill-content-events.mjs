#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import { execute, tool } from "../dist/tools/list-events.js";

const server = new Server(
  { name: "opc-skill-content-events", version: "0.1.0" },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [tool],
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;
  const safeArgs = (args || {}) as Record<string, unknown>;

  if (name === "opc_list_events") {
    return execute(safeArgs as any);
  }

  return {
    content: [
      {
        type: "text",
        text: `❌ 未知工具：${name}`,
      },
    ],
  };
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("[opc-skill-content-events] Server running via stdio");
}

main().catch((error) => {
  console.error("[opc-skill-content-events] Fatal:", error);
  process.exit(1);
});
