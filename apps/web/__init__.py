# coding=utf-8

import os

# import click
from flask import Flask

from apps.web.extensions import db
from apps.web.settings import config

from .errors import register_errors


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask(__name__)

    # 从settings获取配置信息，加载到app.config里
    app.config.from_object(config[config_name])

    # 注册各种模块
    register_extensions(app)
    register_apis(app)
    register_shell_context(app)
    register_commands(app)
    register_errors(app)

    return app


def register_extensions(app):
    db.init_app(app)


def register_apis(app):
    from apps.web.auth.apis import auth_bp
    from apps.web.user.apis import user_bp
    from apps.web.task.apis import task_bp
    app.register_blueprint(auth_bp, url_prefix='/api/v1')
    app.register_blueprint(user_bp, url_prefix='/api/v1')
    app.register_blueprint(task_bp, url_prefix='/api/v1')


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)


def register_commands(app):
    pass