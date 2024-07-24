#ifndef QLITEHTMLWIDGETWRAP_H
#define QLITEHTMLWIDGETWRAP_H

#include <qlitehtmlwidget.h>

class QLITEHTML_EXPORT QLiteHtmlWidgetWrap : public QLiteHtmlWidget
{
    Q_OBJECT
public:
    explicit QLiteHtmlWidgetWrap(QWidget *parent = nullptr);

private:
    QByteArray onResourceHandler(const QUrl &url);
};

#endif // QLITEHTMLWIDGETWRAP_H
