from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    json
)
from flask_login import login_required, login_user, logout_user

from my_flask_app.extensions import login_manager
from my_flask_app.funnels.forms import FunnelForm
from my_flask_app.utils import flash_errors
from my_flask_app.funnels.view_commands import get_funnel_data, create_funnel, get_funnel_stats
from my_flask_app.user.models import Funnel, Cost
from my_flask_app.funnels.funnel_table import get_funnel_table, get_csv

blueprint = Blueprint("manager", __name__, url_prefix="/manage",static_folder="../static")

