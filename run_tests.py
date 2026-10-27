import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from uuid import uuid4

from Config.environment import PROJECT_ROOT


def _run_allure_generate(allure_executable: str, results_dir: Path, report_dir: Path) -> int:
    arguments = [
        allure_executable,
        "generate",
        str(results_dir),
        "--clean",
        "--output",
        str(report_dir),
    ]
    if os.name == "nt" and Path(allure_executable).suffix.lower() in {".bat", ".cmd"}:
        command = subprocess.list2cmdline(arguments)
        return subprocess.run(command, cwd=PROJECT_ROOT, shell=True, check=False).returncode
    return subprocess.run(arguments, cwd=PROJECT_ROOT, check=False).returncode


def main() -> int:
    allure_executable = shutil.which("allure")
    if not allure_executable:
        print(
            "Allure Commandline is required to generate the HTML report. "
            "Install it, then rerun this command.",
            file=sys.stderr,
        )
        return 2

    run_id = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}-{uuid4().hex[:8]}"
    results_dir = PROJECT_ROOT / "reports" / "allure-results" / run_id
    report_dir = PROJECT_ROOT / "reports" / "allure-report" / run_id
    results_dir.mkdir(parents=True, exist_ok=True)

    behave_command = [
        sys.executable,
        "-m",
        "behave",
        "--format",
        "progress",
        "--format",
        "allure_behave.formatter:AllureFormatter",
        "--outfile",
        "-",
        "--outfile",
        str(results_dir),
        *sys.argv[1:],
    ]
    test_result = subprocess.run(behave_command, cwd=PROJECT_ROOT, check=False)
    report_result = _run_allure_generate(allure_executable, results_dir, report_dir)

    if report_result != 0:
        print(f"Allure report generation failed (exit code {report_result}).", file=sys.stderr)
        return report_result

    print(f"Allure results: {results_dir}")
    print(f"Allure HTML report: {report_dir}")
    return test_result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
