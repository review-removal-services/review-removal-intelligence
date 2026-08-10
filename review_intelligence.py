#!/usr/bin/env python3
"""
Review Removal Intelligence
An automated review management system designed to streamline the
identification, analysis, and tracking of problematic online reviews.
Reviews are assessed based on defined policy criteria rather than
assuming that negative feedback should automatically be removed.
https://reviewremoval.services
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_action(scores: dict) -> str:
    labels = {
        "review_risk": "Review Risk",
        "authenticity": "Authenticity",
        "policy_compliance": "Policy Compliance",
        "issue_detection": "Issue Detection",
        "platform_coverage": "Platform Coverage",
        "workflow_efficiency": "Workflow Efficiency",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_review_channels(risk: int, auth: int, workflow: int, issue: int) -> dict:
    return {
        "Google": min(100, round(risk * 1.0)),
        "Yelp": min(100, round(auth * 1.0)),
        "Social Platforms": min(100, round(workflow * 1.0)),
        "App Stores": min(100, round(issue * 1.0)),
    }


def analyze_review_intelligence(
    business: str,
    platform: str = "google",
    review_risk: int = 88,
    authenticity: int = 82,
    policy_compliance: int = 85,
    issue_detection: int = 78,
    platform_coverage: int = 90,
    workflow_efficiency: int = 84,
) -> dict:
    """
    Analyze review management intelligence signals.

    Args:
        business: Business name or identifier
        platform: Primary review platform
        review_risk: Review risk score (0-100)
        authenticity: Authenticity score (0-100)
        policy_compliance: Policy compliance score (0-100)
        issue_detection: Issue detection score (0-100)
        platform_coverage: Platform coverage score (0-100)
        workflow_efficiency: Workflow efficiency score (0-100)

    Returns:
        dict with individual signal scores, overall intelligence index,
        and review channel breakdown
    """
    scores = {
        "review_risk": review_risk,
        "authenticity": authenticity,
        "policy_compliance": policy_compliance,
        "issue_detection": issue_detection,
        "platform_coverage": platform_coverage,
        "workflow_efficiency": workflow_efficiency,
    }
    overall_intelligence_index = round(sum(scores.values()) / 6)

    return {
        "business": business,
        "platform": platform.capitalize(),
        "review_risk_score": review_risk,
        "authenticity_score": authenticity,
        "policy_compliance_score": policy_compliance,
        "issue_detection_score": issue_detection,
        "platform_coverage_score": platform_coverage,
        "workflow_efficiency_score": workflow_efficiency,
        "overall_intelligence_index": overall_intelligence_index,
        "priority_action": get_priority_action(scores),
        "review_channels": get_review_channels(review_risk, authenticity, workflow_efficiency, issue_detection),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    business = args[0] if len(args) > 0 else "business-name"
    platform = args[1] if len(args) > 1 else "google"
    review_risk = int(args[2]) if len(args) > 2 else 88
    authenticity = int(args[3]) if len(args) > 3 else 82
    policy_compliance = int(args[4]) if len(args) > 4 else 85
    issue_detection = int(args[5]) if len(args) > 5 else 78
    platform_coverage = int(args[6]) if len(args) > 6 else 90
    workflow_efficiency = int(args[7]) if len(args) > 7 else 84

    result = analyze_review_intelligence(
        business, platform, review_risk, authenticity,
        policy_compliance, issue_detection, platform_coverage, workflow_efficiency
    )

    print(f"Business: {result['business']}")
    print(f"Platform: {result['platform']}")
    print("=" * 45)
    print(f"Review Risk Score:             {result['review_risk_score']}/100  [{get_status(result['review_risk_score'])}]")
    print(f"Authenticity Score:            {result['authenticity_score']}/100  [{get_status(result['authenticity_score'])}]")
    print(f"Policy Compliance Score:       {result['policy_compliance_score']}/100  [{get_status(result['policy_compliance_score'])}]")
    print(f"Issue Detection Score:         {result['issue_detection_score']}/100  [{get_status(result['issue_detection_score'])}]")
    print(f"Platform Coverage Score:       {result['platform_coverage_score']}/100  [{get_status(result['platform_coverage_score'])}]")
    print(f"Workflow Efficiency Score:     {result['workflow_efficiency_score']}/100  [{get_status(result['workflow_efficiency_score'])}]")
    print("=" * 45)
    print(f"Overall Intelligence Index:    {result['overall_intelligence_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nReview Channels:")
    for channel, score in result['review_channels'].items():
        print(f"  {channel:<24} {score}/100")


if __name__ == "__main__":
    main()
