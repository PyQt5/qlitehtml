#include "qlitehtmlwidgetwrap.h"

QLiteHtmlWidgetWrap::QLiteHtmlWidgetWrap(QWidget *parent)
    : QLiteHtmlWidget(parent)
{
    setResourceHandler(
        std::bind(&QLiteHtmlWidgetWrap::onResourceHandler, this, std::placeholders::_1));
}

QByteArray QLiteHtmlWidgetWrap::onResourceHandler(const QUrl &url)
{
    return QByteArray();
}
