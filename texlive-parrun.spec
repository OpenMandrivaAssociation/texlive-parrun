Name:		texlive-parrun
Version:	15878
Release:	1
Summary:	Typesets (two) streams of text running parallel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/parrun
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parrun.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parrun.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parrun.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
For typesetting translated text and the original source,
parallel on the same page, one above the other.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/parrun/parrun.sty
%doc %{_texmfdistdir}/doc/latex/parrun/parrun.pdf
%doc %{_texmfdistdir}/doc/latex/parrun/readme
#- source
%doc %{_texmfdistdir}/source/latex/parrun/parrun.dtx
%doc %{_texmfdistdir}/source/latex/parrun/parrun.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
