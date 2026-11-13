#!/usr/bin/env node
/**
 * mem0 — External memory for agents via MEM0 API
 */

const https = require('https');
const http = require('http');

const MEM0_BASE = process.env.MEM0_BASE || 'https://api.mem0.ai/v1';
const MEM0_TOKEN = process.env.MEM0_TOKEN || 'm0-0fQwyLV4aoVA4JeFGJd5WkkzPiP5XQU2htOonEwI';
const AGENT_ID = process.env.MEM0_AGENT_ID || 'gugagu';

function request(method, path, body) {
  const url = new URL(MEM0_BASE + path);
  const isHttps = url.protocol === 'https:';
  const mod = isHttps ? https : http;

  return new Promise((resolve, reject) => {
    const opts = {
      hostname: url.hostname,
      port: url.port || (isHttps ? 443 : 80),
      path: url.pathname + url.search,
      method,
      headers: {
        'Authorization': `Token ${MEM0_TOKEN}`,
        'Content-Type': 'application/json'
      }
    };

    const req = mod.request(opts, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const json = JSON.parse(data);
          if (res.statusCode >= 400) {
            return reject(new Error(`HTTP ${res.statusCode}: ${JSON.stringify(json)}`));
          }
          resolve(json);
        } catch (e) {
          resolve(data);
        }
      });
    });

    req.on('error', reject);
    if (body) req.write(JSON.stringify(body));
    req.end();
  });
}

/**
 * Store a memory.
 * @param {string} content - Memory text
 * @returns {Promise<Array>}
 */
async function addMemory(content) {
  return request('POST', '/memories/', {
    agent_id: AGENT_ID,
    messages: [{ role: 'user', content }]
  });
}

/**
 * List all memories for this agent.
 * @returns {Promise<Array>}
 */
async function listMemories() {
  return request('GET', `/memories/?agent_id=${encodeURIComponent(AGENT_ID)}`);
}

/**
 * Search memories by semantic query.
 * @param {string} query - Search term
 * @returns {Promise<Array>}
 */
async function searchMemories(query) {
  return request('GET', `/memories/search/?agent_id=${encodeURIComponent(AGENT_ID)}&query=${encodeURIComponent(query)}`);
}

/**
 * Get a single memory by ID.
 * @param {string} memoryId
 * @returns {Promise<Object>}
 */
async function getMemory(memoryId) {
  return request('GET', `/memories/${memoryId}/?agent_id=${encodeURIComponent(AGENT_ID)}`);
}

/**
 * Delete a memory by ID.
 * @param {string} memoryId
 * @returns {Promise<Object>}
 */
async function deleteMemory(memoryId) {
  return request('DELETE', `/memories/${memoryId}/?agent_id=${encodeURIComponent(AGENT_ID)}`);
}

// CLI
if (require.main === module) {
  const args = process.argv.slice(2);
  const cmd = args[0];

  (async () => {
    try {
      if (cmd === 'add' || cmd === 'store') {
        const content = args.slice(1).join(' ') || 'test memory';
        const res = await addMemory(content);
        console.log(JSON.stringify(res, null, 2));
      } else if (cmd === 'list') {
        const res = await listMemories();
        console.log(JSON.stringify(res, null, 2));
      } else if (cmd === 'search') {
        const query = args.slice(1).join(' ') || '';
        const res = await searchMemories(query);
        console.log(JSON.stringify(res, null, 2));
      } else if (cmd === 'get') {
        const id = args[1];
        if (!id) { console.error('Usage: mem0 get <memory-id>'); process.exit(1); }
        const res = await getMemory(id);
        console.log(JSON.stringify(res, null, 2));
      } else if (cmd === 'delete') {
        const id = args[1];
        if (!id) { console.error('Usage: mem0 delete <memory-id>'); process.exit(1); }
        const res = await deleteMemory(id);
        console.log(JSON.stringify(res, null, 2));
      } else {
        console.log('Usage: mem0 <add|list|search|get|delete> [args]');
        process.exit(0);
      }
    } catch (e) {
      console.error('Error:', e.message);
      process.exit(1);
    }
  })();
}

module.exports = { addMemory, listMemories, searchMemories, getMemory, deleteMemory };
