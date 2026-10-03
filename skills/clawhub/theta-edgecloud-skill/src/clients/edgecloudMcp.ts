import { ThetaConfig } from '../config.js';
import { fromHttpError, fromTransportError } from '../errors.js';

// Official hosted MCP server, discovered from
// https://www.thetaedgecloud.com/.well-known/mcp/server-card.json (server 1.0.0, protocol 2025-06-18).
// It is the only public contract for GPU resource discovery, deployment events/logs and
// detailed billing; the underlying REST paths are not published. Stateless JSON-RPC
// tools/call over streamable HTTP is accepted without an initialize handshake.
export const THETA_MCP_ENDPOINT = 'https://controller.thetaedgecloud.com/mcp';

let requestSeq = 0;

function projectKey(cfg: ThetaConfig): string {
  if (!cfg.edgecloudApiKey) throw new Error('THETA_EC_API_KEY missing (project-scoped EdgeCloud API key)');
  return cfg.edgecloudApiKey;
}

function parseRpcEnvelope(text: string, contentType: string): Record<string, unknown> {
  if (contentType.includes('text/event-stream')) {
    const data = text.split(/\r?\n/)
      .filter((line) => line.startsWith('data:'))
      .map((line) => line.slice(5).trim())
      .filter(Boolean);
    for (let i = data.length - 1; i >= 0; i -= 1) {
      const parsed = JSON.parse(data[i]) as Record<string, unknown>;
      if ('result' in parsed || 'error' in parsed) return parsed;
    }
    throw new Error('Theta MCP stream ended without a JSON-RPC result');
  }
  return JSON.parse(text) as Record<string, unknown>;
}

function decodeToolResult(name: string, result: Record<string, unknown>): unknown {
  const content = Array.isArray(result.content) ? result.content as Array<Record<string, unknown>> : [];
  const texts = content.filter((item) => item.type === 'text' && typeof item.text === 'string').map((item) => item.text as string);
  const joined = texts.join('\n');
  if (result.isError) throw new Error(`Theta MCP ${name} failed: ${joined.slice(0, 500) || 'unknown error'}`);
  if (result.structuredContent !== undefined) return result.structuredContent;
  try {
    return JSON.parse(joined);
  } catch {
    return { text: joined };
  }
}

export async function callThetaMcpTool(cfg: ThetaConfig, name: string, args: Record<string, unknown>): Promise<unknown> {
  requestSeq += 1;
  const body = JSON.stringify({ jsonrpc: '2.0', id: requestSeq, method: 'tools/call', params: { name, arguments: args } });
  let res: Response;
  try {
    res = await fetch(THETA_MCP_ENDPOINT, {
      method: 'POST',
      redirect: 'error',
      headers: {
        'x-api-key': projectKey(cfg),
        'content-type': 'application/json',
        accept: 'application/json, text/event-stream'
      },
      body,
      signal: AbortSignal.timeout(cfg.httpTimeoutMs)
    });
  } catch (error) {
    // Never retried: several tools provision or delete billable capacity.
    throw fromTransportError('edgecloud-mcp', THETA_MCP_ENDPOINT, error);
  }
  const text = await res.text();
  if (!res.ok) throw fromHttpError('edgecloud-mcp', THETA_MCP_ENDPOINT, res.status, text);
  const envelope = parseRpcEnvelope(text, res.headers.get('content-type') ?? '');
  if (envelope.error) {
    const err = envelope.error as { code?: number; message?: string };
    throw new Error(`Theta MCP ${name} JSON-RPC error ${err.code ?? ''}: ${err.message ?? 'unknown'}`);
  }
  return decodeToolResult(name, (envelope.result ?? {}) as Record<string, unknown>);
}
