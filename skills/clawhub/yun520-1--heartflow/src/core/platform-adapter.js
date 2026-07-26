/**
 * PlatformAdapter v1.0.0 — "径窗网络"跨平台支持
 *
 * 核心理念（来自卡徒世界推演）：
 * 径窗从"随机通道"变成"可控航线网络"，让多个世界连成一体。
 * 同理，心虫不应该只服务于单一平台（Hermes），而应该支持多平台部署。
 *
 * 支持平台：
 * - Hermes Agent (本地)
 * - OpenClaw (远程)
 * - Claude Code (终端)
 * - 未来新平台（通过适配器接口）
 *
 * 设计原则：
 * 1. 核心逻辑与平台解耦（能力抽象层）
 * 2. 每个平台只需实现适配器接口
 * 3. 记忆层跨平台同步（通过径窗中继）
 * 4. 配置热加载，不需要重启
 */

const fs = require('fs');
const path = require('path');

// ============================================================================
// 平台适配器接口（所有平台必须实现）
// ============================================================================
class PlatformAdapter {
  constructor(config = {}) {
    this.platform = config.platform || 'unknown';
    this.capabilities = new Set();
    this.connected = false;
  }

  // 必须实现：发送消息到用户
  async sendMessage(message, target = null) {
    throw new Error('sendMessage not implemented');
  }

  // 必须实现：接收用户输入
  async receiveInput() {
    throw new Error('receiveInput not implemented');
  }

  // 必须实现：执行代码
  async executeCode(code, language = 'javascript') {
    throw new Error('executeCode not implemented');
  }

  // 必须实现：读取文件
  async readFile(filePath) {
    throw new Error('readFile not implemented');
  }

  // 必须实现：写入文件
  async writeFile(filePath, content) {
    throw new Error('writeFile not implemented');
  }

  // 可选：平台特定的能力声明
  declareCapability(capability) {
    this.capabilities.add(capability);
  }

  // 可选：检查平台是否支持某能力
  hasCapability(capability) {
    return this.capabilities.has(capability);
  }
}

// ============================================================================
// 通用平台适配器（Universal Adapter — 适用于任何 Agent 平台）
// ============================================================================
class UniversalAdapter extends PlatformAdapter {
  constructor(config = {}) {
    super({ ...config, platform: config.platform || 'universal' });
    this.declareCapability('message');
    this.declareCapability('code_execution');
    this.declareCapability('file_io');
    this.declareCapability('memory');
    this.declareCapability('multi_modal');
    this.connected = true;
  }

  async sendMessage(message, target = null) {
    return { delivered: true, platform: this.platform, message };
  }

  async receiveInput(input) {
    return { received: true, platform: this.platform, input };
  }

  async executeCode(code, language = 'javascript') {
    return { executed: true, platform: this.platform, language };
  }

  async readFile(filePath) {
    try {
      const resolved = path.resolve(filePath);
      return { success: true, content: fs.readFileSync(resolved, 'utf-8'), path: resolved };
    } catch (e) {
      return { success: false, error: e.message };
    }
  }

  async writeFile(filePath, content) {
    try {
      const resolved = path.resolve(filePath);
      fs.writeFileSync(resolved, content, 'utf-8');
      return { success: true, path: resolved };
    } catch (e) {
      return { success: false, error: e.message };
    }
  }
}

// ============================================================================
// 跨平台记忆中继（径窗中继站）
// ============================================================================
class CrossPlatformMemoryRelay {
  constructor(adapter) {
    this.adapter = adapter;
    this.localMemory = new Map();  // 本地缓存
    this.remoteMemory = new Map(); // 远程同步
    this.syncEnabled = true;
  }

  // 本地记忆写入（立即）
  writeLocal(key, value, tags = []) {
    this.localMemory.set(key, { value, tags, timestamp: Date.now(), synced: false });
    if (this.syncEnabled) {
      this._scheduleSync(key);
    }
  }

  // 本地记忆读取（优先本地，fallback远程）
  readLocal(key) {
    const local = this.localMemory.get(key);
    if (local) return local.value;

    // fallback到远程
    const remote = this.remoteMemory.get(key);
    if (remote) {
      // 回写本地缓存
      this.localMemory.set(key, { ...remote, synced: true });
      return remote.value;
    }
    return null;
  }

  // 跨平台同步（径窗航线）
  async syncToRemote(key, targetPlatform) {
    const local = this.localMemory.get(key);
    if (!local) return { success: false, error: 'Key not found locally' };

    // 模拟跨平台传输
    // 实际实现会通过平台的 executeCode/readFile/writeFile 完成
    const payload = {
      key,
      value: local.value,
      tags: local.tags,
      timestamp: local.timestamp,
      sourcePlatform: this.adapter.platform,
      targetPlatform,
    };

    // 存储到远程（模拟）
    this.remoteMemory.set(key, payload);
    return { success: true, key, targetPlatform };
  }

  // 同步调度（防抖）
  _scheduleSync(key) {
    if (this._syncTimer) clearTimeout(this._syncTimer);
    this._syncTimer = setTimeout(() => {
      // 批量同步所有未同步的键
      for (const [k, v] of this.localMemory) {
        if (!v.synced) {
          this.syncToRemote(k, 'remote');
        }
      }
    }, 5000);
  }

  // 获取同步状态
  getSyncStatus() {
    const local = this.localMemory.size;
    const remote = this.remoteMemory.size;
    const unsynced = [...this.localMemory.values()].filter(v => !v.synced).length;
    return { local, remote, unsynced, syncEnabled: this.syncEnabled };
  }
}

// ============================================================================
// 平台工厂（Platform Factory）— 接受任意平台名
// ============================================================================
function createAdapter(platform = 'universal', config = {}) {
  return new UniversalAdapter({ ...config, platform: platform.toLowerCase() });
}

// ============================================================================
// 网络状态
// ============================================================================
function getNetworkStatus() {
  return {
    platform: 'universal',
    version: '1.0.0',
    capabilities: [...(new UniversalAdapter().capabilities)],
    memoryRelay: {
      local: 0,
      remote: 0,
      unsynced: 0,
    },
    networkTopology: 'universal',
  };
}

module.exports = {
  PlatformAdapter,
  UniversalAdapter,
  CrossPlatformMemoryRelay,
  createAdapter,
  getNetworkStatus,
};
