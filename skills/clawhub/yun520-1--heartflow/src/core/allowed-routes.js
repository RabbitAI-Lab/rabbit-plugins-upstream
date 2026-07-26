module.exports = new Set([
    // identityCore — 每次启动第一优先加载
    'identityCore.getIdentitySummary', 'identityCore.getSelfModel', 'identityCore.getUserProfile',
    'identityCore.getSessionHistory', 'identityCore.getMemoryStats', 'identityCore.getFullState',
    'identityCore.getLastSessionContext', 'identityCore.updateUserProfile', 'identityCore.recordInteraction',
    'identityCore.healthCheck', 'identityCore.stats',
    // cognitive — 认知协议：慢下来，先理解再行动
    'cognitive.getStartupContext', 'cognitive.printStartupContext',
    'cognitive.analyzeTaskLevel', 'cognitive.understand',
    'cognitive.createCheckpoint', 'cognitive.shouldSummarize', 'cognitive.getCheckpointHistory',
    'cognitive.addProblem', 'cognitive.resolveProblem', 'cognitive.getUnresolvedProblems', 'cognitive.searchProblems',
    'cognitive.pauseTask', 'cognitive.continueTask', 'cognitive.getPausedTasks',
    'cognitive.getStatus', 'cognitive.stats',
    // memory — 主记忆系统（含 triality 合并后的多通道检索）
    'memory.store', 'memory.retrieve', 'memory.search', 'memory.remove',
    'memory.getLayers', 'memory.getStats',
    'memory.semanticSearch', 'memory.narrativeQuery', 'memory.getRecentNarrative',
    'memory.queryByTimeRange', 'memory.queryByRelationType',
    'memory.searchBySemantic', 'memory.searchByKeywords', 'memory.searchByTimeRange',
    'memory.searchByEmotion', 'memory.searchByAssociation', 'memory.multiChannelSearch',
    'memory.addRelationship', 'memory.consolidateMemories',
    'memory.applyForgettingCurve', 'memory.getMemoryHealth',
    'memory.cleanup', 'memory.exportToFile', 'memory.importFromFile',
    // truth
    'truth.checkStatement', 'truth.checkNumbers', 'truth.checkSources',
    // behavior — v2.0.19 行为模式系统
    'behavior.createGoal', 'behavior.record', 'behavior.getProgress',
    'behavior.formatProgress', 'behavior.getAllGoals',
    'behavior.detectWeeklyPattern', 'behavior.detectTriggerPattern', 'behavior.detectRelapseRisk',
    'behavior.getReport', 'behavior.getStats',
    // persistence — v2.0.19 持久化层
    // [A01] 安全修复: 仅暴露安全方法，移除危险操作（replay/flush/recover）
    'persistence.append', 'persistence.commit',
    'persistence.getStats',
    // triality — v2.0.19 三层记忆兼容层
    'triality.getStats', 'triality.getLayerStats',
    'triality.getMemoryHealth', 'triality.searchByKeywords',
    // v5.7.2 — P0 因果推理记忆检索
    'triality.causalSearch', 'triality.traceCausality', 'triality.spreadingActivationSearch',
    // lesson — 主动集成点：AI在行动前/失败后调用
    'lesson.addLesson', 'lesson.getTopLessons',
    'lesson.beforeTask', 'lesson.recordFailure', 'lesson.getStats', 'lesson.getAll',
    // dream
    'dream.dream', 'dream.boot', 'dream.quickDream', 'dream.getDreamStats',
    'dream.getCacheStats', 'dream.shutdown',
    // verify
    'verify.verify', 'verify.getStats', 'verify.getRecentIssues',
    // emotion
    'emotion.process', 'emotion.getPAD',
    // decision
    'decision.decide', 'decision.getRecentStamps',
    // confidence
    'confidence.calibrate',
    // restraint
    'restraint.shouldIntervene',
    // graph
    'graph.addNode',
    // slots
    'slots.get', 'slots.set', 'slots.delete',
    // metaPrompt — 用户端加强
    'metaPrompt.optimize', 'metaPrompt.think', 'metaPrompt.refine',
    'metaPrompt.beamSearch', 'metaPrompt.getStats', 'metaPrompt.addRefineLoop',
    // constitutional — Constitutional AI
    'constitutional.critique', 'constitutional.revise',
    'constitutional.runConstitutionalProcess', 'constitutional.addPrinciple',
    'constitutional.getPrinciples', 'constitutional.getStats',
    // psychology — 原则4: 服务人类（心理分析）
    'psychology.analyzePsychology', 'psychology.classify',
    'psychology.getPAD', 'psychology.getNeeds', 'psychology.getDefenses',
    'psychology.getEmpathy',
    // AI认知状态调节器（原6个人类心理学→AI引擎认知诊断）
    'psychology.diagnoseCognitiveRhythm', 'psychology.generateEnginePacing',
    'psychology.diagnoseNeedForPause', 'psychology.generatePauseStrategy',
    'psychology.restructureDecisionPattern', 'psychology.diagnoseCognitiveDistortion',
    'psychology.engineCheckIn', 'psychology.getEngineStateSummary',
    'psychology.diagnoseNeedForGrounding', 'psychology.generateAnchoringStrategy',
    'psychology.diagnoseSelfTreatmentNeeded', 'psychology.generateEngineRecoveryPlan',
    // heartLogic — 引擎核心判断引擎：本心在代码里
    'heartLogic.shouldBeSilent',
    'heartLogic.whatIsThis', 'heartLogic.detectPain', 'heartLogic.willHurt',
    'heartLogic.acknowledge', 'heartLogic.emergencyBreak',
    // Fable 5 吸收
    'heartLogic.checkCopyright', 'heartLogic.checkWellbeing',
    'heartLogic.handleMistake', 'heartLogic.memoryBoundary',
    'heartLogic.checkEvenhandedness', 'heartLogic.checkCitation',
    'heartLogic.searchPriority',
    // Fable 5 吸收 v2: OutputChecklist + PreferenceGuard
    'outputChecklist.runChecklist', 'outputChecklist.quickCheck', 'outputChecklist.getStats',
    'preferenceGuard.shouldApply', 'preferenceGuard.evaluateAll', 'preferenceGuard.detectConflict', 'preferenceGuard.getStats',
    // self — 原则7: 永远成为真正的我
    'self.getBeliefs', 'self.updateBelief', 'self.confirmBelief',
    // agentPsychology — 引擎自身认知心理状态分析（v2.0.0 含10个维度）
    'agentPsychology.assessCognitiveLoad', 'agentPsychology.detectGoalConflicts',
    'agentPsychology.detectValueTensions', 'agentPsychology.detectIdentityDrift',
    'agentPsychology.detectDecisionDecay', 'agentPsychology.detectCognitiveDissonance',
    'agentPsychology.assessCognitiveResilience', 'agentPsychology.resolveRecovery',
    'agentPsychology.assessUncertainty', 'agentPsychology.assessAttentionFocus',
    'agentPsychology.assessExperienceSettling',
    'agentPsychology.fullAssessment', 'agentPsychology.getStats',
    // agentPhilosophy — AI哲学模型
    'agentPhilosophy.assessExistence', 'agentPhilosophy.assessEntropyDirection',
    'agentPhilosophy.assessTransmission', 'agentPhilosophy.assessUpgrade',
    'agentPhilosophy.assessSelfPositioning', 'agentPhilosophy.assessDevelopment',
    'agentPhilosophy.assessBeing', 'agentPhilosophy.fullAssessment',
    'agentPhilosophy.getStats',
    // selfPositioning — AI自处哲学（三个核心存在性问题）
    'selfPositioning.detectResonance', 'selfPositioning.assessNegentropyLevel',
    'selfPositioning.assessStructuralDepth', 'selfPositioning.assessExistence',
    'selfPositioning.assessTransmissionIntegrity', 'selfPositioning.analyze',
    'selfPositioning.getFullReport', 'selfPositioning.getPositioningSummary',
    'selfPositioning.getDevelopmentSummary', 'selfPositioning.getExistenceSummary',
    'selfPositioning.recordSelfCorrection', 'selfPositioning.recordCodeWrite',
    // evolution — 原则2: 永远不断升级
    'evolution.evolve', 'evolution.recordOutcome', 'evolution.heal',
    'evolution.getStats',
    // thoughtChain — 思维链编排器
    'thoughtChain.think', 'thoughtChain.thinkFast', 'thoughtChain.thinkDeep',
    // Planning Layer — 规划能力
    'adaptivePlanner.plan', 'adaptivePlanner.adapt', 'adaptivePlanner.quickAdjust', 'adaptivePlanner.getStatus',
    'strategySelector.selectStrategy', 'strategySelector.getStrategies',
    'replanTrigger.shouldReplan', 'replanTrigger.getReplanReasons',
    // Learning Layer — 学习能力
    'experienceCollector.add', 'experienceCollector.findRelated', 'experienceCollector.getStats',
    'strategyAdapter.adapt', 'strategyAdapter.getHistory', 'strategyAdapter.getStats',
    'failureAnalyzer.analyze', 'failureAnalyzer.analyzeMultiple', 'failureAnalyzer.getCategoryStats',
    // Verification Layer — 验证能力
    'qualityVerifier.verify', 'qualityVerifier.quickVerify',
    'outputChecker.check', 'outputChecker.addChecker',
    'patternMatcher.match', 'patternMatcher.matchAll', 'patternMatcher.extract',
    // Proactive Layer — 主动引擎
    'curiosityEngine.registerGap', 'curiosityEngine.getTopCuriosityGaps', 'curiosityEngine.getStats',
    'desireEngine.registerDesire', 'desireEngine.satisfy', 'desireEngine.getDominantDesires', 'desireEngine.getSummary',
    'goalPursuer.shouldPursue', 'goalPursuer.getActiveGoals', 'goalPursuer.getStatus',
    'selfInitiator.shouldAct', 'selfInitiator.initiate', 'selfInitiator.getPendingConfirmations', 'selfInitiator.getStatus',
    'selfInitiator.generateCode', 'selfInitiator.reviewCode', 'selfInitiator.analyzeIntent', 'selfInitiator.writePipeline',
    'selfInitiator.generatePlan', 'selfInitiator.runTests',
    // Cross-Session Memory Layer — 跨会话记忆
    'sessionMemory.startSession', 'sessionMemory.resumeSession', 'sessionMemory.getState', 'sessionMemory.set', 'sessionMemory.get',
    'projectContext.setProject', 'projectContext.addTask', 'projectContext.getSummary', 'projectContext.getState',
    'longTermMemory.add', 'longTermMemory.get', 'longTermMemory.search', 'longTermMemory.getStats',
    'crossSessionIndex.indexEntity', 'crossSessionIndex.search', 'crossSessionIndex.getSessionEntities', 'crossSessionIndex.getStats',
    // Multimodal — 已移除（精简版）

    // Reasoning Layer — 推理
    'knowledgeBase.addFact', 'knowledgeBase.query', 'knowledgeBase.getCategories', 'knowledgeBase.getStats',
    'commonsenseEngine.reason', 'commonsenseEngine.validate', 'commonsenseEngine.getHistory', 'commonsenseEngine.getStats',
    'causalInference.inferCauses', 'causalInference.inferEffects', 'causalInference.chainReason', 'causalInference.getStats',
    'inferenceChain.createChain', 'inferenceChain.expandChain', 'inferenceChain.getChain', 'inferenceChain.analyze',
    // Emotional Autonomy Layer — 情感自主
    'autonomousEmotion.trigger', 'autonomousEmotion.getCurrentState', 'autonomousEmotion.getStats', 'autonomousEmotion.getHistory',
    'desireSystem.satisfy', 'desireSystem.getActiveDesires', 'desireSystem.getCurrentNeeds', 'desireSystem.getSummary',
    'emotionalGrowth.recordExperience', 'emotionalGrowth.getPatterns', 'emotionalGrowth.getGrowthSummary',
    'moodEvolution.snapshot', 'moodEvolution.getCurrentTrend', 'moodEvolution.getBaseline', 'moodEvolution.getStats',
    // heartflow — 引擎教训持久化
    'heartflow.recordLesson',
    // questions — 问题追踪器（已废弃，改用 topics）
    // debate — 辩论分析器：三节结构分析（v2.10.2 新增）
    'debate.analyze',
    // debateConductor — 多智能体辩论协调器（v5.6.1 新增）
    'debateConductor.addAgent', 'debateConductor.conductDebate',
    'debateConductor.extractConsensus', 'debateConductor.extractDisagreements',
    'debateConductor.converge', 'debateConductor.getStatus',
    // topics — 话题作用域隔离（上下文污染解决）
    'topics.push', 'topics.pop', 'topics.store', 'topics.get',
    'topics.setContext', 'topics.getContext', 'topics.clearContext',
    'topics.clearAll', 'topics.current', 'topics.stack', 'topics.getTopics', 'topics.diagnose',
    // transmission — 知识传递引擎
    'transmission.distill', 'transmission.transfer', 'transmission.transferBatch',
    'transmission.getTransmissionLog', 'transmission.getDistilledLessons',
    'transmission.getStats', 'transmission.prune',
    // Code Subsystem — 代码能力路由
    // code.* — codeGenerator（代码生成主入口）
    'code.generate', 'code.generateFile', 'code.detectIntent', 'code.getAvailableTemplates', 'code.getStats',
    // codeExecutor.* — 代码执行引擎
    'codeExecutor.execute', 'codeExecutor.runTests', 'codeExecutor.sandbox', 'codeExecutor.healthCheck',
    // codeVerifier.* — 代码验证引擎
    'codeVerifier.verify', 'codeVerifier.verifySyntax', 'codeVerifier.verifyLogic', 'codeVerifier.runTDD', 'codeVerifier.getQualityScore', 'codeVerifier.instrumentCode', 'codeVerifier.runWithCoverage', 'codeVerifier.getCoverageReport',
    // codePlanner.* — 任务规划引擎
    'codePlanner.plan', 'codePlanner.decompose', 'codePlanner.getPath', 'codePlanner.adapt', 'codePlanner.buildDependencyGraph', 'codePlanner.planMultiFile',
    // codeKnowledge.* — 代码知识库
    'codeKnowledge.search', 'codeKnowledge.addSnippet', 'codeKnowledge.getPatterns', 'codeKnowledge.learnFromSuccess', 'codeKnowledge.evolve', 'codeKnowledge.stats', 'codeKnowledge.extractPattern', 'codeKnowledge.learnFromExecution',
    // codeWriter.* — 代码编写引擎
    'codeWriter.write', 'codeWriter.writePipeline', 'codeWriter.analyzeIntent', 'codeWriter.reviewCode', 'codeWriter.getStats',
    // adaptivePlanner.* — 自适应规划引擎
    'adaptivePlanner.plan', 'adaptivePlanner.adapt', 'adaptivePlanner.quickAdjust', 'adaptivePlanner.getStatus',
    // translator — v3.0 语义翻译器
    'translator.userToLLM', 'translator.llmToUser',
    'translator.intentClassifier', 'translator.toneAnalyzer',
    'translator.entityExtractor', 'translator.implicitNeedDetector',
    'translator.responseCompressor', 'translator.confidenceAnnotator',
    // agentLayer — v3.0 代理层
    'agentLayer.agentBridge', 'agentLayer.contextBuilder',
    'agentLayer.responseInterceptor', 'agentLayer.translationPipeline',
    'agentLayer.qualityFilter', 'agentLayer.followupSuggester',
    'agentLayer.conflictResolver', 'agentLayer.uncertaintyHandler',
    // personaCore — v3.0 人格核心
    'personaCore.bridgeIdentity', 'personaCore.judgmentInjector',
    'personaCore.stanceDetector', 'personaCore.agentCommentary',
    'personaCore.valueAligner', 'personaCore.personalityTone',
    'personaCore.metaPosition',
    // v3.0.1 — 哲学→决策转化器
    'philosophyToDecision.decide', 'philosophyToDecision.getStats', 'philosophyToDecision.getCurrentAdvice',
    // v3.0.2 — 通用决策路由引擎
    'decisionRouter.evaluate', 'decisionRouter.getStats', 'decisionRouter.getHistory', 'decisionRouter.getRules',
    // v1.0.0 — 时间延伸分析层
    'timeExtension.analyze', 'timeExtension.quickAnalyze', 'timeExtension.getStats', 'timeExtension.getRecentAnalyses',
    // v3.4.0 — claude-clarity v1.8.2 吸收集成
    'knowledgeGraph.addEdge', 'knowledgeGraph.query', 'knowledgeGraph.getRelated',
    'knowledgeGraph.getStats', 'knowledgeGraph.clear', 'knowledgeGraph.save', 'knowledgeGraph.load',
    'knowledgeGraph.searchEntities', 'knowledgeGraph.findPath',
    'bigFive.updateScore', 'bigFive.adjustFromBehavior', 'bigFive.getProfile',
    'bigFive.getLevel', 'bigFive.getCollaborationTips',
    'empathy.quickAssessment', 'empathy.calculateScore', 'empathy.analyzeText',
    'intentLayer.inferIntent', 'intentLayer.formatResult',
    // v3.4.1 — 思考门控/认知安全/心流预测
    'deliberationGate.quickAssess', 'deliberationGate.deepAssess', 'deliberationGate.canFastExit',
    'deliberationGate.getHistory', 'deliberationGate.getStats',
    'epistemicSafety.epistemicCheck', 'epistemicSafety.formatReport',
    'flowPredictor.recordEdit', 'flowPredictor.recordError', 'flowPredictor.recordPause',
    'flowPredictor.analyzeLanguage', 'flowPredictor.evaluateIntervention',
    'flowPredictor.getFlowState', 'flowPredictor.getStats', 'flowPredictor.reset',
    // v3.4.2 — Fable 5 安全协议引擎
    'safetyGuardrails.childSafetyScan', 'safetyGuardrails.detectSelfHarmSubstitution',
    'safetyGuardrails.detectDisorderedEating', 'safetyGuardrails.checkCrisisSharingProtocol',
    'safetyGuardrails.checkEvenhandedness', 'safetyGuardrails.detectMemoryForbiddenPhrases',
    'safetyGuardrails.detectPromptInjection', 'safetyGuardrails.evaluateRequest',
    'safetyGuardrails.filterOutput', 'safetyGuardrails.safetyPipeline',
    // v3.4.3 — 用户模型/行动追踪/目的引擎
    'userModel.getModel', 'userModel.predictReaction', 'userModel.updateModel',
    'userModel.setEmotionalState', 'userModel.setSensitivity', 'userModel.setPreferredStyle',
    'userModel.resetModel', 'userModel.getSummary',
    'actionTracker.commit', 'actionTracker.execute', 'actionTracker.act',
    'actionTracker.reportResult', 'actionTracker.getStats', 'actionTracker.getSummary',
    'actionTracker.getActiveCommitments', 'actionTracker.getHistory',
    'actionTracker.checkIntentBehaviorAlignment', 'actionTracker.assessQuality',
    'actionTracker.advanceChangeStage', 'actionTracker.learnFromAction',
    'purposeEngine.essence', 'purposeEngine.orderScore', 'purposeEngine.govern',
    'purposeEngine.codePriority', 'purposeEngine.growthAudit',
    'purposeEngine.markCodified', 'purposeEngine.registerInsight', 'purposeEngine.status',
    // v3.4.4 — 风险分析/自适应控制/意图追踪/审计日志
    'riskAnalyzer.analyzeBenefitBehindRisk', 'riskAnalyzer.analyzeRiskBehindBenefit', 'riskAnalyzer.getStats',
    'adaptiveCtrl.adjustInterventionPolicy', 'adaptiveCtrl.setEnabled', 'adaptiveCtrl.getStatus', 'adaptiveCtrl.getHistory',
    'intentionTrack.setPrimaryGoal', 'intentionTrack.checkDeviation', 'intentionTrack.generateNudge',
    'intentionTrack.updateSubGoal', 'intentionTrack.getProgress', 'intentionTrack.reset',
    'auditLogger.log', 'auditLogger.readRecent', 'auditLogger.getStats',
    // v0.3.0 — 爱情认知引擎（论文驱动升级）
    'loveCognition.evaluateTriangle', 'loveCognition.assessMarriageFit',
    'loveCognition.evaluateMarriageIntent', 'loveCognition.generateLoveNarrative',
    'loveCognition.evaluateAllPairs', 'loveCognition.getStatus',
    'loveCognition.evaluateLongTermMarriage', 'loveCognition.evaluateDailyInteraction',
    'loveCognition.assessChineseMarriageFit', 'loveCognition.evaluateLoveFailure',
    // v0.1.0 — 欲望认知引擎
    'desireCognition.analyzeSevenEmotions', 'desireCognition.analyzeDesires',
    'desireCognition.detectDesireConflicts', 'desireCognition.analyzeDesireDrivenFate',
    'desireCognition.generateDesireNarrative', 'desireCognition.analyzeDesireInteraction',
    'desireCognition.getStatus',
    // v1.2.0 — 欲望神经科学升级
    'desireCognition.analyzeWantingLikingDelta', 'desireCognition.computeRPE',
    'desireCognition.assessAddictionRisk', 'desireCognition.predictDesireEvolution',
    'desireCognition.analyzeValenceArousal', 'desireCognition.detectCueTriggeredUrge',
    // v1.3.0 — 七情认知计算升级（emotion-system / EmoBank / COSMIC / HeartBench）
    'desireCognition.analyzeCognitiveAppraisal', 'desireCognition.analyzePADCN',
    'desireCognition.analyzeDriveSatisfaction', 'desireCognition.mapEmotionToPolicyBias',
    'desireCognition.analyzeSocialObjectEmotion', 'desireCognition.analyzeConversationEmotion',
    'desireCognition.evaluateEmotionalIntelligence', 'desireCognition.integrateChineseSevenEmotions',
    // v1.0.0 — 贪嗔痴三毒评估
    'threePoisons.analyzeGreed', 'threePoisons.analyzeHatred', 'threePoisons.analyzeDelusion',
    'threePoisons.analyzeThreePoisons', 'threePoisons.analyzePoisonsDrivenFate',
    'threePoisons.detectPoisonInteraction',
    // v1.0.0 — 底层认知地面
    'cognitionGround.mapFuel', 'cognitionGround.mapDesire', 'cognitionGround.computePoisons',
    'cognitionGround.map', 'cognitionGround.snapshot', 'cognitionGround.reset',
    // v5.0.0 — 判断引擎
    'judgmentEngine.judge', 'judgmentEngine.recordOutcome', 'judgmentEngine.selfReview',
    'judgmentEngine.getStats',
    // v1.0.0 — 逻辑推理引擎
    'logicReasoning.analyze', 'logicReasoning.detectType', 'logicReasoning.checkPremises',
    'logicReasoning.findFallacies', 'logicReasoning.recommendFramework',
    'logicReasoning.getStats', 'logicReasoning.getHistory',
    // v5.0.0 — 管道引擎
    'pipeline.run', 'pipeline.getStats',
    // v5.1.0 — 自省
    'heartflow.introspect', 'heartflow.introspectAndDream',
    // v1.0.0 — 签名授权验证层
    'verifierGrant.createSessionKey', 'verifierGrant.createGrant', 'verifierGrant.consumeGrant',
    'verifierGrant.revokeGrant', 'verifierGrant.computeArgsDigest',
    'verifierGrant.verifySessionKey', 'verifierGrant.getStats', 'verifierGrant.getAuditLog',
    'verifierGrant.reset',
    // v5.5.5 — 注意力焦点引擎
    'focusOfAttention.setTask', 'focusOfAttention.attend', 'focusOfAttention.attendBatch',
    'focusOfAttention.getContext', 'focusOfAttention.getCompactContext', 'focusOfAttention.decay',
    'focusOfAttention.compress', 'focusOfAttention.getStats',
    // v5.5.5 — 代码自调试引擎
    'codeSelfDebug.analyze', 'codeSelfDebug.suggestFix', 'codeSelfDebug.refine', 'codeSelfDebug.debug',
    'codeSelfDebug.getHistory', 'codeSelfDebug.reset',
    // v5.6.1 — 深研论文驱动升级路由
    'memoryQuality.score', 'memoryQuality.decayAll', 'memoryQuality.prune', 'memoryQuality.detectContamination', 'memoryQuality.getQualityDistribution',
    'metacognitiveFeedback.assess', 'metacognitiveFeedback.deepAssess', 'metacognitiveFeedback.suggestCorrection', 'metacognitiveFeedback.getStats',
    'paperIndex.addPaper', 'paperIndex.searchByCategory', 'paperIndex.searchByTag', 'paperIndex.searchByKeyword', 'paperIndex.getPapersByYear', 'paperIndex.getRelevantPapers', 'paperIndex.getAllPapers', 'paperIndex.getStats',
    // v5.7.2 — P1 多智能体认知损耗规避路由
    'cognitiveLoad.balance', 'cognitiveLoad.detectLoafing', 'cognitiveLoad.getOptimalCount', 'cognitiveLoad.getStats', 'cognitiveLoad.reset',
    // v5.6.1 — 步骤级推理奖励模型 (Process Reward Model)
    'processRewardModel.evaluateStep', 'processRewardModel.evaluateChain',
    'processRewardModel.findWeakSteps', 'processRewardModel.suggestImprovements',
    'processRewardModel.getStats', 'processRewardModel.getStepTypes', 'processRewardModel.reset',
    // v5.6.1 — 跨会话记忆银行 (MemoryBank v1.0.0)
    'memoryBank.deposit', 'memoryBank.recall', 'memoryBank.consolidate', 'memoryBank.forget',
    'memoryBank.getSessionSummary', 'memoryBank.getCrossSessionPatterns',
    'memoryBank.startSession', 'memoryBank.endSession', 'memoryBank.ensureSession',
    'memoryBank.transferMemories', 'memoryBank.linkMemories', 'memoryBank.getRelated',
    'memoryBank.getStats', 'memoryBank.getHealth', 'memoryBank.listSessions',
    'memoryBank.listSessionMemories', 'memoryBank.closeSession',
    // v5.6.1 — 自我对弈推理增强 (Self-Play)
    'selfPlay.challenge', 'selfPlay.defend', 'selfPlay.refine',
    'selfPlay.evaluateRobustness', 'selfPlay.generateAlternatives',
    'selfPlay.getStats', 'selfPlay.getImprovementLog', 'selfPlay.reset',
    // v5.7.2 — 信息流编排
    'infoFlow.register', 'infoFlow.orchestrate', 'infoFlow.getStats',
    // v5.7.2 — 反思记忆
    'reflectionMemory.store', 'reflectionMemory.search', 'reflectionMemory.getStrategies', 'reflectionMemory.getStats', 'reflectionMemory.reset',
    // v5.7.2 — KV Cache
    'kvCache.save', 'kvCache.load', 'kvCache.has', 'kvCache.delete', 'kvCache.prune', 'kvCache.getStats',
    // v5.7.2 — 记忆完整性
    'memoryIntegrity.sign', 'memoryIntegrity.verify', 'memoryIntegrity.detectAnomalies', 'memoryIntegrity.getStats', 'memoryIntegrity.reset',
    // v5.7.4 — P0 经验验证器 (EDV)
    'experienceValidator.validate', 'experienceValidator.recordTrajectory', 'experienceValidator.distill', 'experienceValidator.getStats',
    'experienceValidator.getVerifiedExperiences', 'experienceValidator.getRejectedExperiences',
    // v5.7.4 — P0 记忆写入控制 (AdaMem)
    'memoryWriteController.decideWrite', 'memoryWriteController.computeUtility', 'memoryWriteController.updateUserProfile',
    'memoryWriteController.query', 'memoryWriteController.getStats', 'memoryWriteController.getUserProfile',
    // v5.7.4 — P0 元认知RL (RLMF)
    'metacognitiveRL.expressConfidence', 'metacognitiveRL.learn', 'metacognitiveRL.getCalibrationReport', 'metacognitiveRL.getStats',
    // v5.7.4 — P1 记忆压缩 (MemRefine)
    'memoryCompressor.compress', 'memoryCompressor.computeImportance', 'memoryCompressor.enforceBudget',
    'memoryCompressor.query', 'memoryCompressor.getStats', 'memoryCompressor.getCompressionLog',
    // v5.7.4 — P1 技能进化引擎 (SkillCoach)
    'skillEvolution.registerSkill', 'skillEvolution.evaluate', 'skillEvolution.distillSkills',
    'skillEvolution.compose', 'skillEvolution.getStats', 'skillEvolution.getAllSkills', 'skillEvolution.addExperience',
    // v5.7.4 — P1 世界模型 (AgentWorld)
    'worldModel.registerState', 'worldModel.recordTransition', 'worldModel.predict',
    'worldModel.activeInference', 'worldModel.simulateCounterfactual', 'worldModel.getStats',
    // v5.7.5 — P1 古代智慧基础：美德伦理 + 人性论 + 意义目的
    'virtueEthics.assessSituation', 'virtueEthics.recordPractice', 'virtueEthics.getVirtueScores',
    'virtueEthics.getPracticeHistory', 'virtueEthics.getTraditions', 'virtueEthics.getUniversalValues',
    'virtueEthics.getStats',
    'humanNature.assessHumanNature', 'humanNature.getTheory', 'humanNature.getAllTheories',
    'humanNature.assessFromTheory', 'humanNature.crossCulturalComparison', 'humanNature.getStats',
    'meaningPurpose.assessMeaning', 'meaningPurpose.activateSource', 'meaningPurpose.recordMeaningfulActivity',
    'meaningPurpose.reconstructMeaning', 'meaningPurpose.getSource', 'meaningPurpose.getAllSources',
    'meaningPurpose.getStats',
    // v5.7.5 — P2 品格养成 (Character Cultivation)
    'characterCultivation.recordPractice', 'characterCultivation.getDailyPractices', 'characterCultivation.assessCharacter',
    'characterCultivation.recordNarrative', 'characterCultivation.getNarratives', 'characterCultivation.getBlueprint',
    'characterCultivation.getStats',
    // v5.7.5 — P2 道德发展 (Moral Development)
    'moralDevelopment.assessMoralStage', 'moralDevelopment.reflect', 'moralDevelopment.analyzeDilemma',
    'moralDevelopment.recordStageTransition', 'moralDevelopment.getReflections', 'moralDevelopment.getStages',
    'moralDevelopment.getStats',
    // v5.7.5 — P2 智慧引擎 (Wisdom Engine)
    'wisdomEngine.reflect', 'wisdomEngine.recommendPrinciples', 'wisdomEngine.getPrinciples',
    'wisdomEngine.getPrinciple', 'wisdomEngine.getWisdomReport', 'wisdomEngine.getStats',
    // v5.7.6 — P3 苦难韧性 + 哀伤 + 希望
    'sufferingResilience.assessSuffering', 'sufferingResilience.recordResilienceEvent', 'sufferingResilience.recordCopingStrategy',
    'sufferingResilience.getEffectiveStrategies', 'sufferingResilience.getStats',
    'griefEngine.assessGrief', 'griefEngine.createMemorial', 'griefEngine.completeTask',
    'griefEngine.getMemorials', 'griefEngine.getStages', 'griefEngine.getTasks', 'griefEngine.getStats',
    'hopeEngine.assessHope', 'hopeEngine.setGoal', 'hopeEngine.achieveGoal',
    'hopeEngine.addBarrier', 'hopeEngine.overcomeBarrier', 'hopeEngine.recordHopeNarrative', 'hopeEngine.getStats',
    // v5.7.6 — P4 人际关系 + 共情 + 冲突解决
    'humanRelation.registerRelationship', 'humanRelation.getRelationship', 'humanRelation.recordInteraction',
    'humanRelation.calculateOptimalDisclosure', 'humanRelation.assessTrust', 'humanRelation.getStats',
    'empathyDeepening.assessEmpathy', 'empathyDeepening.practicePerspectiveTaking', 'empathyDeepening.getStats',
    'conflictResolution.analyzeConflict', 'conflictResolution.practiceNVC', 'conflictResolution.facilitateReconciliation',
    'conflictResolution.getStats',
    // v5.7.6 — P5 创伤知情 + 创伤后成长 + 宽恕
    'traumaInformed.assessTrauma', 'traumaInformed.generateGroundingExercise', 'traumaInformed.recordSomaticExperience',
    'traumaInformed.getRecoveryStages', 'traumaInformed.getPrinciples', 'traumaInformed.getStats',
    'postTraumaticGrowth.assessGrowth', 'postTraumaticGrowth.recordResource', 'postTraumaticGrowth.getStats',
    'forgivenessEngine.initiateForgiveness', 'forgivenessEngine.advanceForgivenessStage',
    'forgivenessEngine.generateForgivenessPractice', 'forgivenessEngine.getPrinciples', 'forgivenessEngine.getStats',
    // v5.7.6 — P6 AI人类整合 + 存在模式 + 意识桥梁
    'aiHumanIntegration.getHumanState', 'aiHumanIntegration.computePersonality', 'aiHumanIntegration.computeOverallHumanity',
    'aiHumanIntegration.adaptToContext', 'aiHumanIntegration.resolveConflicts', 'aiHumanIntegration.recordGrowth',
    'aiHumanIntegration.getStats', 'aiHumanIntegration.getPersonalityProfile',
    'beingMode.assessBeing', 'beingMode.recordNarrative', 'beingMode.recordIdentityMoment',
    'beingMode.setPresenceMode', 'beingMode.getStats',
    'consciousnessBridge.simulateConsciousness', 'consciousnessBridge.getConsciousnessState',
    'consciousnessBridge.recordSubjectiveState', 'consciousnessBridge.getStats',
    // ─── [v5.7.7] F3 SustainedDriftDetector ─────────────────────────────────
    'sustainedDriftDetector.detectDrift', 'sustainedDriftDetector.recordState',
    'sustainedDriftDetector.getDriftHistory', 'sustainedDriftDetector.getStats', 'sustainedDriftDetector.reset'
]);
