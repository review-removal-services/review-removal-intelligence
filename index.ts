#!/usr/bin/env node

interface ReviewIntelligenceInput {
  business: string;
  platform: string;
  reviewRisk: number;
  authenticity: number;
  policyCompliance: number;
  issueDetection: number;
  platformCoverage: number;
  workflowEfficiency: number;
}

interface ReviewIntelligenceOutput {
  business: string;
  platform: string;
  reviewRiskScore: number;
  authenticityScore: number;
  policyComplianceScore: number;
  issueDetectionScore: number;
  platformCoverageScore: number;
  workflowEfficiencyScore: number;
  overallIntelligenceIndex: number;
  priorityAction: string;
  reviewChannels: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    reviewRisk: "Review Risk",
    authenticity: "Authenticity",
    policyCompliance: "Policy Compliance",
    issueDetection: "Issue Detection",
    platformCoverage: "Platform Coverage",
    workflowEfficiency: "Workflow Efficiency",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getReviewChannels(risk: number, auth: number, workflow: number, issue: number): Record<string, number> {
  return {
    "Google": Math.min(100, Math.round(risk * 1.0)),
    "Yelp": Math.min(100, Math.round(auth * 1.0)),
    "Social Platforms": Math.min(100, Math.round(workflow * 1.0)),
    "App Stores": Math.min(100, Math.round(issue * 1.0)),
  };
}

export function analyzeReviewIntelligence(input: ReviewIntelligenceInput): ReviewIntelligenceOutput {
  const scores = {
    reviewRisk: input.reviewRisk,
    authenticity: input.authenticity,
    policyCompliance: input.policyCompliance,
    issueDetection: input.issueDetection,
    platformCoverage: input.platformCoverage,
    workflowEfficiency: input.workflowEfficiency,
  };
  const overallIntelligenceIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    business: input.business,
    platform: input.platform.charAt(0).toUpperCase() + input.platform.slice(1),
    reviewRiskScore: input.reviewRisk,
    authenticityScore: input.authenticity,
    policyComplianceScore: input.policyCompliance,
    issueDetectionScore: input.issueDetection,
    platformCoverageScore: input.platformCoverage,
    workflowEfficiencyScore: input.workflowEfficiency,
    overallIntelligenceIndex,
    priorityAction: getPriorityAction(scores),
    reviewChannels: getReviewChannels(input.reviewRisk, input.authenticity, input.workflowEfficiency, input.issueDetection),
  };
}

const args = process.argv.slice(2);
const business = args[0] || "business-name";
const platform = args[1] || "google";
const reviewRisk = parseInt(args[2]) || 88;
const authenticity = parseInt(args[3]) || 82;
const policyCompliance = parseInt(args[4]) || 85;
const issueDetection = parseInt(args[5]) || 78;
const platformCoverage = parseInt(args[6]) || 90;
const workflowEfficiency = parseInt(args[7]) || 84;

const result = analyzeReviewIntelligence({
  business, platform, reviewRisk, authenticity,
  policyCompliance, issueDetection, platformCoverage, workflowEfficiency,
});

console.log(`Business: ${result.business}`);
console.log(`Platform: ${result.platform}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Review Risk Score:             ${result.reviewRiskScore}/100  [${getStatus(result.reviewRiskScore)}]`);
console.log(`Authenticity Score:            ${result.authenticityScore}/100  [${getStatus(result.authenticityScore)}]`);
console.log(`Policy Compliance Score:       ${result.policyComplianceScore}/100  [${getStatus(result.policyComplianceScore)}]`);
console.log(`Issue Detection Score:         ${result.issueDetectionScore}/100  [${getStatus(result.issueDetectionScore)}]`);
console.log(`Platform Coverage Score:       ${result.platformCoverageScore}/100  [${getStatus(result.platformCoverageScore)}]`);
console.log(`Workflow Efficiency Score:     ${result.workflowEfficiencyScore}/100  [${getStatus(result.workflowEfficiencyScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Intelligence Index:    ${result.overallIntelligenceIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nReview Channels:");
Object.entries(result.reviewChannels).forEach(([channel, score]) => {
  console.log(`  ${channel.padEnd(22)} ${score}/100`);
});
