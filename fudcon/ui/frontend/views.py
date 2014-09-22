# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g, url_for
from fudcon.modules.contents.models import Content
from fudcon.modules.speakers.models import Speaker
from fudcon.modules.sessions.models import Session
from fudcon.app import app

bp = Blueprint('frontend', __name__,
               template_folder='templates')

items_per_page = app.config['ITEMS_PER_PAGE']


@bp.route('/', methods=['GET', 'POST'])
def index():
    queryset = Content.query.filter(Content.is_on_user_menu == 1,
                                    Content.tag == 'home',
                                    Content.active == 1).first()
    return render_template('frontend/index.html',
                           title="Home",
                           detail=queryset)


@bp.route('/venue', methods=['GET', 'POST'])
def venue():
    queryset = Content.query.filter(Content.is_on_user_menu == 1,
                                    Content.tag == 'venue',
                                    Content.active == 1).first()
    return render_template('frontend/index.html',
                           title='Venue',
                           detail=queryset)


@bp.route('/accomodation', methods=['GET', 'POST'])
def accomodation():
    queryset = Content.query.filter(Content.is_on_user_menu == 1,
                                    Content.tag == 'accomodation',
                                    Content.active == 1).first()
    return render_template('frontend/index.html',
                           title='Alojamiento',
                           detail=queryset)


@bp.route('/sponsors', methods=['GET', 'POST'])
def sponsors():
    queryset = Content.query.filter(Content.is_on_user_menu == 1,
                                    Content.tag == 'sponsors',
                                    Content.active == 1).first()
    return render_template('frontend/index.html',
                           title='Sponsors',
                           detail=queryset)


@bp.route('/speakers', methods=['GET', 'POST'])
@bp.route('/speakers/<int:page>', methods=['GET', 'POST'])
def speakers(page=1):
    paginate_params = (page, items_per_page, False)
    queryset = Speaker.query.filter(Speaker.active == 1).paginate(*paginate_params)
    return render_template('frontend/speakers.html',
                           title=u'Ponentes',
                           speakers=queryset)


@bp.route('/sessions', methods=['GET', 'POST'])
@bp.route('/sessions/<int:page>', methods=['GET', 'POST'])
def sessions(page=1):
    """Ui for session.

    :page: parameter for pagination
    :returns: a template for session

    """
    # paginate_params = (page, items_per_page, False)
    # queryset = Session.query.paginate(*paginate_params)
    talks = Session.query.filter(Session.active == 1,
                                 Session.session_type == 1).all()
    barcamps = Session.query.filter(Session.active == 1,
                                    Session.session_type == 2).all()
    workshops = Session.query.filter(Session.active == 1,
                                     Session.session_type == 3).all()
    return render_template('frontend/sessions.html', 
                           title=u'Sesiones',
                           talks=talks,
                           barcamps=barcamps,
                           workshops=workshops)
