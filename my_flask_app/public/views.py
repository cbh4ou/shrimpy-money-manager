# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, login_user, logout_user, current_user

from my_flask_app.extensions import login_manager
from my_flask_app.public.forms import LoginForm
from my_flask_app.user.forms import RegisterForm
from my_flask_app.user.models import User
from my_flask_app.utils import flash_errors

blueprint = Blueprint("public", __name__, static_folder="../static")


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route("/", methods=["GET"])
@login_required
def home():
    """Home page."""
    if current_user.is_authenticated:
        return render_template("public/newhome.html")
    else:
        return redirect(url_for("public.login"))

@blueprint.route("/logout")
def logout():
    """Logout."""
    logout_user()
    flash("You are logged out.", "info")
    return redirect(url_for("public.login"))

@blueprint.route("/login", methods=["GET", "POST"])
def login():
    """Login."""
    
    if current_user.is_authenticated:
        return redirect(url_for("public.home"))
    form = LoginForm(request.form)
    current_app.logger.info("Hello from the home page!")
    # Handle logging in
    if request.method == "POST":
        if form.validate_on_submit():
            login_user(form.user, remember=form.remember_me.data)
            flash("You are logged in.", "success")
            redirect_url = request.args.get("next") or url_for("public.home")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("users/login.html", form=form)


@blueprint.route("/register", methods=["GET", "POST"])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            active=True,
        )
        flash("Thank you for registering. You can now log in.", "success")
        return redirect(url_for("public.login"))
    else:
        flash_errors(form)
    return render_template("public/register.html", form=form)


@blueprint.route("/about/")
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template("public/about.html", form=form)

@blueprint.route("/costs")
@login_required
def global_costs():
    """About page."""
    return render_template("public/costs.html")



@blueprint.route("/404")
def test():
    """About page."""

    return render_template("404.html")

@blueprint.route("/401")
def auth_redirect():

    return redirect(url_for("public.login"))