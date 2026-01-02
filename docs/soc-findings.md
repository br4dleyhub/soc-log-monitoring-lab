## SOC Findings

The detection system identified a potential brute-force attack
against user "alice".

Multiple failed authentication attempts followed by a successful
login triggered an alert.

This behavior matches known brute-force attack patterns.

## Severity Assessment

Severity: Medium

The activity is suspicious but not conclusively malicious.
No lateral movement or data exfiltration was observed.

## Recommended SOC Actions
- Monitor the affected account
- Enforce stronger authentication controls
- Review historical login behavior

## Reflection

This project demonstrated how SOC teams transform logs into
alerts and actionable insights.

It highlighted the importance of correlation, threshold tuning,
and avoiding alert fatigue.
