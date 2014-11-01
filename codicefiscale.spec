#%%define debug_package	%{nil}

Name: 		codicefiscale
Summary: 	The tax code in Italy is an alphanumeric code
Version: 	1.2
Release: 	1
License: 	LGPLv3
Group: 		Office
URL:		https://github.com/kratos83/CodiceFiscale
Source0:	%{name}-%{version}.tar.gz
# desktop is a real mess.Sflo
Patch0:		%{name}-1.1-desktop.patch
# we don't install in /opt.Sflo
Patch1:		%{name}-1.1-install.patch
BuildRequires:	qt4-devel 
BuildRequires:	desktop-file-utils
# this is being seen as the same %name...
Conflicts:		texlive-codicefiscaleitaliano


%description
The tax code in Italy is an alphanumeric code with a fixed 
length of 16 characters, inspired by the use of library, 
which is used to uniquely identify the tax and 
administrative citizens, non-recognized associations, 
taxpayers and foreigners born and domiciled the 
Italian territory. The tax code is assigned at birth
or the constitution for associations. 
For all taxpayers not subject individuals 
with a VAT (trust, permanent establishments, 
societies, associations recognized, foundations) 
normally also has the same function of the tax code. 
For companies registered in the register of companies, 
although all have a tax code, according to the law, 
the identifier is the legal Rea, even if not used by the Revenue.

%prep
%setup -q
%patch0 -p0 -b desktop.
%patch1 -p0 -b install.
find . -type f -exec chmod -x {} \;

%build
%qmake_qt4
%make 

%install
%makeinstall INSTALL_ROOT=%{buildroot}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop 
chmod -x %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc licenza.txt README.md comuni.txt stati.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*.png

