Name:		texlive-bezos
Version:	20101014
Release:	1
Summary:	Packages by Javier Bezos
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bezos
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bezos.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bezos.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A set of packages that provide: - tools for maths accents; - a
tool that changes page-numbering in frontmatter to arabic; -
tools for dealing with some annoyances in babel; - a tool for
making end-environment checking more meaningful; - tensorial
indexes; - support for multi-file documents; - tools for easy
entry of Spanish index entries; and - dotless i's and j's for
maths fonts.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bezos/accents.sty
%{_texmfdistdir}/tex/latex/bezos/arabicfront.sty
%{_texmfdistdir}/tex/latex/bezos/babeltools.sty
%{_texmfdistdir}/tex/latex/bezos/checkend.sty
%{_texmfdistdir}/tex/latex/bezos/dotlessi.sty
%{_texmfdistdir}/tex/latex/bezos/esindex.sty
%{_texmfdistdir}/tex/latex/bezos/subdocs.sty
%{_texmfdistdir}/tex/latex/bezos/tensind.sty
%doc %{_texmfdistdir}/doc/latex/bezos/README
%doc %{_texmfdistdir}/doc/latex/bezos/accents.pdf
%doc %{_texmfdistdir}/doc/latex/bezos/accents.tex
%doc %{_texmfdistdir}/doc/latex/bezos/babeltools.pdf
%doc %{_texmfdistdir}/doc/latex/bezos/babeltools.tex
%doc %{_texmfdistdir}/doc/latex/bezos/bezos.pdf
%doc %{_texmfdistdir}/doc/latex/bezos/bezos.tex
%doc %{_texmfdistdir}/doc/latex/bezos/esindex.pdf
%doc %{_texmfdistdir}/doc/latex/bezos/esindex.tex
%doc %{_texmfdistdir}/doc/latex/bezos/tensind.pdf
%doc %{_texmfdistdir}/doc/latex/bezos/tensind.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
