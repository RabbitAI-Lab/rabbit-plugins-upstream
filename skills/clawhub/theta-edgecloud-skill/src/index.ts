import { loadConfig } from './config.js';
import { deployments } from './commands/deployments.js';
import { inference } from './commands/inference.js';
import { video } from './commands/video.js';
import { ondemand } from './commands/ondemand.js';
import { healthCheck } from './commands/health.js';
import {
  executeThetaRuntimeCommand,
  listThetaRuntimeCommands,
  thetaRuntimeCommandSchemas,
  thetaCommandRequiresConfirm,
  type ThetaRuntimeCommandArgs,
  type ThetaRuntimeContext
} from './runtime/handlers.js';
import {
  resolveThetaOnDemandToken,
  type ThetaSecretResolverContext
} from './runtime/secretResolver.js';

// Read-only convenience facade. Resource mutations (deployments, RAG agents, video,
// characters, GPU nodes) are reachable only through executeThetaRuntimeCommand, which
// enforces confirm:true outside dry-run.
export function theta() {
  const cfg = loadConfig();
  return {
    cfg,
    deploy: {
      listStandard: deployments.listStandard,
      listCustom: deployments.listCustom,
      listVm: deployments.listVm,
      list: deployments.list,
      routeProbe: deployments.routeProbe,
      balance: deployments.balance,
      chatbotGet: deployments.chatbotGet,
      chatbotList: deployments.chatbotList,
      chatbotDocumentGet: deployments.chatbotDocumentGet,
      chatbotDocumentList: deployments.chatbotDocumentList
    },
    inference,
    video: {
      videoGet: video.videoGet,
      videoList: video.videoList,
      streamGet: video.streamGet,
      ingestorList: video.ingestorList
    },
    ondemand,
    healthCheck: () => healthCheck(cfg)
  };
}

export {
  executeThetaRuntimeCommand,
  listThetaRuntimeCommands,
  thetaRuntimeCommandSchemas,
  thetaCommandRequiresConfirm,
  resolveThetaOnDemandToken
};

export type {
  ThetaRuntimeCommandArgs,
  ThetaRuntimeContext,
  ThetaSecretResolverContext
};
