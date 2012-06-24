Summary:	Pen - load-balancer
Summary(pl):	Pen - narz�dzie do rozk�adania obci��enia
Name:		pen
Version:	0.17.1
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://siag.nu/pub/pen/%{name}-%{version}.tar.gz
# Source0-md5:	62548155d3bf42aea05b32227e132331
URL:		http://siag.nu/pen/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is pen, a load balancer for "simple" TCP based protocols such as
HTTP or SMTP. It allows several servers to appear as one to the
outside and automatically detects servers that are down and
distributes clients among the available servers. This gives high
availability and scalable performance.

%description -l pl
pen to narz�dzie do rozk�adania obci��enia (load balancer) dla
protoko��w opartych o TCP, takich jak HTTP czy SMTP. Pozwala na
udost�pnienie kilku serwer�w na zewn�trz tak, aby wygl�da�y na jeden
oraz automatycznie wykrywa serwery wy��czone i rozprowadza klient�w po
dost�pnych serwerach. Daje to wysok� dost�pno�� i skalowaln�
wydajno��.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HOWTO README penstats
%attr(755,root,root) %{_bindir}/mergelogs
%attr(755,root,root) %{_bindir}/pen
%attr(755,root,root) %{_bindir}/penctl
%attr(755,root,root) %{_bindir}/penlog
%attr(755,root,root) %{_bindir}/penlogd
%{_mandir}/man1/mergelogs.1*
%{_mandir}/man1/pen.1*
%{_mandir}/man1/penctl.1*
%{_mandir}/man1/penlog.1*
%{_mandir}/man1/penlogd.1*
