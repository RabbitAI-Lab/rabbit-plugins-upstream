import { ThetaConfig } from '../config.js';
import { thetaVideoClient } from '../clients/thetaVideo.js';

export const video = {
  uploadCreate: (cfg: ThetaConfig) => cfg.dryRun ? { dryRun: true } : thetaVideoClient.createUploadSession(cfg),
  videoCreate: (cfg: ThetaConfig, payload: Record<string, unknown>) => cfg.dryRun ? { dryRun: true, payload } : thetaVideoClient.createVideo(cfg, payload),
  videoGet: (cfg: ThetaConfig, videoId: string) => thetaVideoClient.getVideo(cfg, videoId),
  videoList: (cfg: ThetaConfig, serviceAccountId: string, page = 1, number = 10) => thetaVideoClient.listVideos(cfg, serviceAccountId, page, number),
  streamCreate: (cfg: ThetaConfig, payload: Record<string, unknown>) => cfg.dryRun ? { dryRun: true, payload } : thetaVideoClient.createStream(cfg, payload),
  streamGet: (cfg: ThetaConfig, streamId: string) => thetaVideoClient.getStream(cfg, streamId),
  ingestorList: (cfg: ThetaConfig) => thetaVideoClient.listIngestors(cfg),
  ingestorSelect: (cfg: ThetaConfig, ingestorId: string, body: Record<string, unknown>) => cfg.dryRun ? { dryRun: true, ingestorId, body } : thetaVideoClient.selectIngestor(cfg, ingestorId, body)
};
