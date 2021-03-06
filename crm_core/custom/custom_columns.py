import django_tables2 as tables


class ButtonColumn(tables.TemplateColumn):

    def __init__(self, text="", onclick="location.href='#'", gl_icon=None, extra_class="btn-default", **extra):
        glyph_icon = ""
        if gl_icon:
            glyph_icon = "<span class='glyphicon glyphicon-%s' aria-hidden='true'></span> " % gl_icon
        extra['template_code'] = """<button type="button" class="btn btn-sm %s pull-right" onclick="%s">%s%s</button>""" \
                                 % (extra_class, onclick, glyph_icon, text)
        super(ButtonColumn, self).__init__(**extra)


class ImageLinkColumn(tables.TemplateColumn):

    def __init__(self, link="#", img=None, **extra):
        extra['template_code'] = """<a href="%s"><img src="%s" /></a>""" % (link, img)
        super(ImageLinkColumn, self).__init__(**extra)


class RelatedModelDetailLinkColumn(tables.TemplateColumn):

    def __init__(self, **extra):
        extra['template_code'] = """<a href="{{ value.get_absolute_url }}">{{ value }}</a>"""
        super(RelatedModelDetailLinkColumn, self).__init__(**extra)


class LabelColumn(tables.TemplateColumn):

    def __init__(self, **extra):
        extra['template_code'] = """
        <span class="label label-{{ record.get_state_class }}">{{ record.get_state }}</span>"""
        super(LabelColumn, self).__init__(**extra)


class ButtonsColumn(tables.TemplateColumn):

    def __init__(self, btn_list, **extra):
        html_code = """<div class="btn-group btn-group-sm" role="group">"""
        for btn in list(btn_list):
            glyph_icon = extra_class = onclick = text = ""
            condition = '1'
            if 'gl_icon' in btn:
                glyph_icon = "<span class='glyphicon glyphicon-%s' aria-hidden='true'></span> " % btn['gl_icon']
            if 'extra_class' in btn:
                extra_class = btn['extra_class']
            if 'onclick' in btn:
                onclick = btn['onclick']
            if 'text' in btn:
                text = btn['text']
            if 'condition' in btn:
                condition = "record." + btn['condition']
            html_code += "{% if " + condition + " %}"
            html_code += """<button type="button" class="btn %s" onclick="%s">%s%s</button>""" \
                         % (extra_class, onclick, glyph_icon, text)
            html_code += "{% endif %}"
        html_code += """</div>"""
        extra['template_code'] = html_code
        super(ButtonsColumn, self).__init__(**extra)