import pytest

pytest.main(["-s", "-v",
             "--html=report.html"])  # 收集所在目录下的所有用例并执行。
